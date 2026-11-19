#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""COMSOL 5.3 2D image packager for the MOS interactive HTML (offline).

Input: Image.zip with Image/{Electron,Hole,EF,EP}/{kind}0001..1586.png
   or: an extracted Image folder with the same structure.
Output: images/{electron,hole,field,potential}/tox_05/vg_-2.0.png, etc.

Only uses the Python standard library. Does not resize images or alter their pixels.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import re
import shutil
import struct
import sys
import tempfile
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

N_THICKNESSES = 26
N_VOLTAGES = 61
COUNT_PER_KIND = N_THICKNESSES * N_VOLTAGES
SOURCE_KINDS = {"electron": "electron", "hole": "hole", "ef": "field", "ep": "potential"}
PREFIXES = {"electron": "Electron", "hole": "Hole", "field": "EF", "potential": "EP"}
EXPECTED_KINDS = ("electron", "hole", "field", "potential")
PNG_SIG = b"\x89PNG\r\n\x1a\n"


@dataclass(frozen=True)
class Frame:
    kind: str
    index: int
    source_name: str
    handle: object
    width: int
    height: int

    @property
    def tox(self) -> int:
        return 5 + (self.index - 1) // N_VOLTAGES

    @property
    def voltage(self) -> float:
        tenth = -20 + (self.index - 1) % N_VOLTAGES
        return tenth / 10.0

    @property
    def relative_path(self) -> str:
        return f"{self.kind}/tox_{self.tox:02d}/vg_{self.voltage:.1f}.png"


def parse_source_name(raw_name: str) -> tuple[str, int] | None:
    """Return (website kind, numbered frame) from COMSOL's actual zip layout."""
    path = PurePosixPath(raw_name.replace("\\", "/"))
    if path.suffix.lower() != ".png":
        return None
    folder_name = path.parent.name.lower()
    kind = SOURCE_KINDS.get(folder_name)
    if kind is None:
        return None
    # e.g. Image/EF/EF0001.png; for alternate COMSOL names, only the number matters
    # as long as it is safely contained in the correct quantity folder.
    match = re.fullmatch(r"([a-z][a-z _-]*?)(\d{1,6})", path.stem, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"Cannot identify numbered PNG in {folder_name}: {raw_name}")
    prefix = re.sub(r"[ _-]", "", match.group(1)).lower()
    if prefix != PREFIXES[kind].lower():
        raise ValueError(
            f"Unexpected prefix in {raw_name}; expected {PREFIXES[kind]}0001.png etc."
        )
    return kind, int(match.group(2))


def png_size(header: bytes, name: str) -> tuple[int, int]:
    if len(header) < 24 or header[:8] != PNG_SIG or header[12:16] != b"IHDR":
        raise ValueError(f"Not a valid PNG header: {name}")
    w, h = struct.unpack(">II", header[16:24])
    if w <= 0 or h <= 0:
        raise ValueError(f"Invalid PNG dimensions: {name}")
    return w, h


class Source:
    def __init__(self, path: Path):
        self.path = path
        self.zip: zipfile.ZipFile | None = None

    def __enter__(self):
        if self.path.is_file() and self.path.suffix.lower() == ".zip":
            self.zip = zipfile.ZipFile(self.path)
        elif not self.path.is_dir():
            raise ValueError("--source must be a ZIP file or an extracted folder")
        return self

    def __exit__(self, *_):
        if self.zip:
            self.zip.close()

    def entries(self):
        if self.zip:
            for info in self.zip.infolist():
                if not info.is_dir() and info.filename.lower().endswith(".png"):
                    yield info.filename, info
        else:
            for path in sorted(self.path.rglob("*")):
                if path.is_file() and not path.is_symlink() and path.suffix.lower() == ".png":
                    yield str(path.relative_to(self.path)).replace(os.sep, "/"), path

    def read_head(self, handle) -> bytes:
        if self.zip:
            with self.zip.open(handle) as f:
                return f.read(24)
        with handle.open("rb") as f:
            return f.read(24)

    def copy_with_hash(self, handle, out: Path) -> str:
        digest = hashlib.sha256()
        with self.zip.open(handle) if self.zip else handle.open("rb") as src:
            with out.open("wb") as dst:
                while block := src.read(1024 * 1024):
                    dst.write(block)
                    digest.update(block)
        return digest.hexdigest()


def inspect(source: Source, expected_size: tuple[int, int] | None):
    all_frames: dict[str, dict[int, Frame]] = {k: {} for k in EXPECTED_KINDS}
    ignored = 0
    dimensions: dict[str, Counter] = defaultdict(Counter)
    for path, handle in source.entries():
        parsed = parse_source_name(path)
        if parsed is None:
            ignored += 1
            continue
        kind, idx = parsed
        if not 1 <= idx <= COUNT_PER_KIND:
            raise ValueError(f"Out-of-range index {idx} in {path}, expected 1..{COUNT_PER_KIND}")
        if idx in all_frames[kind]:
            raise ValueError(f"Duplicate index {idx} for {kind}: {path}")
        w, h = png_size(source.read_head(handle), path)
        dimensions[kind][(w, h)] += 1
        if expected_size is not None and (w, h) != expected_size:
            raise ValueError(f"Wrong size {w}x{h} for {path}; expected {expected_size[0]}x{expected_size[1]}")
        all_frames[kind][idx] = Frame(kind, idx, path, handle, w, h)
    for kind in EXPECTED_KINDS:
        present = all_frames[kind]
        missing = sorted(set(range(1, COUNT_PER_KIND + 1)) - set(present))
        if missing:
            sample = ", ".join(map(str, missing[:12]))
            raise ValueError(
                f"{kind}: {len(present)}/{COUNT_PER_KIND} images. Missing indices: {sample}"
                + (" ..." if len(missing) > 12 else "")
            )
    if ignored:
        print(f"[INFO] Ignored {ignored} unrelated PNG(s) outside Electron/Hole/EF/EP folders.")
    for kind in EXPECTED_KINDS:
        size_description = ", ".join(f"{w}x{h}: {count}" for (w, h), count in sorted(dimensions[kind].items()))
        if len(dimensions[kind]) != 1:
            print(f"[WARNING] {kind} has mixed dimensions; web image slot will still preserve aspect ratio.")
        print(f"[OK] {kind:9} {len(all_frames[kind]):4d} files | {size_description}")
    print("[OK] Index mapping: #1 = 5 nm/-2.0 V, #61 = 5 nm/+4.0 V, "
          "#62 = 6 nm/-2.0 V, #1586 = 30 nm/+4.0 V")
    return all_frames


def write_package(source: Source, frames: dict[str, dict[int, Frame]], output: Path, manifest: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    manifest.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(tempfile.mkdtemp(prefix=".comsol_images_v9_", dir=output.parent))
    manifest_tmp = manifest.with_name(manifest.name + ".tmp")
    backup_dir = output.with_name(output.name + ".v9_backup")
    try:
        with manifest_tmp.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["kind", "source_path", "index", "tox_nm", "Vg_V", "Vd_V",
                             "website_path", "width_px", "height_px", "sha256"])
            n = 0
            for kind in EXPECTED_KINDS:
                for idx in range(1, COUNT_PER_KIND + 1):
                    frame = frames[kind][idx]
                    dst = temp_dir / frame.relative_path
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    sha = source.copy_with_hash(frame.handle, dst)
                    writer.writerow([kind, frame.source_name, idx, frame.tox, f"{frame.voltage:.1f}",
                                     "0.1", f"images/{frame.relative_path}", frame.width,
                                     frame.height, sha])
                    n += 1
                print(f"[COPIED] {kind}: {COUNT_PER_KIND} images")
        # Atomic directory replacement on same volume, with rollback on failure.
        if backup_dir.exists():
            raise ValueError(f"Backup folder already exists: {backup_dir}. Rename it before retrying.")
        had_previous = output.exists()
        if had_previous:
            output.rename(backup_dir)
        try:
            temp_dir.rename(output)
        except Exception:
            if had_previous and backup_dir.exists():
                backup_dir.rename(output)
            raise
        manifest_tmp.replace(manifest)
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        print(f"[DONE] {n} images in: {output}")
        print(f"[DONE] Full mapping + SHA-256: {manifest}")
    finally:
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        if manifest_tmp.exists():
            manifest_tmp.unlink()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=Path, help="Your Image.zip or extracted Image folder")
    parser.add_argument("--output", type=Path, help="Website images directory (default: <script>/images)")
    parser.add_argument("--manifest", type=Path, help="Mapping CSV (default: <script>/COMSOL_Image_Manifest.csv)")
    parser.add_argument("--check-only", action="store_true", help="Verify input names, counts, and PNG sizes without copying")
    parser.add_argument("--strict-size", default=None, help="Fail if images differ from WxH, e.g. 1280x600")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent
    if args.source:
        src = args.source.expanduser().resolve()
    elif (root / "Image.zip").is_file():
        src = root / "Image.zip"
    elif (root / "Image").is_dir():
        src = root / "Image"
    else:
        parser.error("No Image.zip found. Put it beside organize_images.py, or use --source PATH")
    output = (args.output or (root / "images")).expanduser().resolve()
    manifest = (args.manifest or (root / "COMSOL_Image_Manifest.csv")).expanduser().resolve()
    expected = None
    if args.strict_size:
        match = re.fullmatch(r"(\d+)[xX](\d+)", args.strict_size)
        if not match:
            parser.error("--strict-size must be written as WIDTHxHEIGHT, e.g. 1280x600")
        expected = tuple(map(int, match.groups()))
    if not src.exists():
        parser.error(f"Source not found: {src}")
    print(f"[SOURCE] {src}")
    try:
        with Source(src) as source:
            frames = inspect(source, expected)
            if args.check_only:
                print("[PASS] 6,344 images validated; no files were changed.")
            else:
                write_package(source, frames, output, manifest)
        return 0
    except (ValueError, OSError, zipfile.BadZipFile, RuntimeError) as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
