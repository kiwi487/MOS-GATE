#!/usr/bin/env python3
"""Read-only v10.7 validator. Website ships without optional 6,344 COMSOL PNG frames."""
from pathlib import Path
from html.parser import HTMLParser
import csv, hashlib, struct, sys
BASE=Path(__file__).resolve().parent
REQUIRE='--require-images' in sys.argv

for name in ('index.html','MOS_COMSOL_Offline.html','organize_images.py','COMSOL_Methodology.md',
             'report/Untitled.html','report/Untitled_files/report.css'):
    if not (BASE/name).is_file(): raise SystemExit(f'FAIL: missing {name}')
if (BASE/'index.html').read_bytes() != (BASE/'MOS_COMSOL_Offline.html').read_bytes():
    raise SystemExit('FAIL: two website entrypoints differ')

class ReportRefs(HTMLParser):
    def __init__(self): super().__init__();self.images=[];self.styles=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='img' and 'src' in a:self.images.append(a['src'])
        if tag=='link' and 'stylesheet' in (a.get('rel') or '') and 'href' in a:self.styles.append(a['href'])
refs=ReportRefs();refs.feed((BASE/'report/Untitled.html').read_text(encoding='utf-8'))
if len(refs.images)!=71:raise SystemExit(f'FAIL: expected 71 report images, got {len(refs.images)}')
for rel in refs.images+refs.styles:
    path=(BASE/'report'/rel).resolve()
    if not path.is_relative_to((BASE/'report').resolve()) or not path.is_file():
        raise SystemExit(f'FAIL: missing/unsafe report asset {rel}')
html=(BASE/'index.html').read_text(encoding='utf-8')
if html.count('href="report/Untitled.html"')!=1 or html.count('Original COMSOL model (.mph) · Google Drive')!=1:
    raise SystemExit('FAIL: two source links not found in Chapter 05')
if 'href="COMSOL_Methodology.md"' in html or 'href="COMSOL_Report.zip"' in html:
    raise SystemExit('FAIL: old report/notes link remains')
print('PASS: direct HTML report with 71 figures and local CSS; two model-source links.')

image_dir=BASE/'images'
if not image_dir.exists():
    if REQUIRE: raise SystemExit('FAIL: images/ is required but not present')
    print('PASS: HTML mirrors and organizer present; images/ intentionally omitted (add your own later).')
    sys.exit(0)

manifests=[BASE/'COMSOL_Image_Manifest.csv',
           BASE/'evidence/manifests/COMSOL_Image_Manifest_1280x600_UPLOADED_UNVERIFIED.csv']
first_image=next(image_dir.rglob('*.png'),None)
if first_image is None:raise SystemExit('FAIL: images/ exists but contains no PNGs')
with first_image.open('rb') as f: head=f.read(24)
if len(head)<24 or head[:8]!=b'\x89PNG\r\n\x1a\n': raise SystemExit('FAIL: invalid PNG header')
dims=struct.unpack('>II',head[16:24])
manifest=None
for candidate in manifests:
    if not candidate.exists():continue
    with candidate.open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=6344:continue
    expected=tuple(int(rows[0][k]) for k in ('width_px','height_px'))
    if expected==dims:
        manifest=candidate;break
if manifest is None:
    raise SystemExit(f'FAIL: PNG dimensions {dims} do not match the supplied 654x480 or 1280x600 manifest')
errors=[]
for n,row in enumerate(rows,1):
    file=BASE/row['website_path']
    if not file.is_file():
        errors.append(f'{n}: MISSING {file}')
    else:
        with file.open('rb') as f:
            header=f.read(24)
            if len(header)<24 or header[:8]!=b'\x89PNG\r\n\x1a\n':errors.append(f'{n}: invalid PNG {file}')
            else:
                wh=struct.unpack('>II',header[16:24])
                if wh!=(int(row['width_px']),int(row['height_px'])):errors.append(f'{n}: dimensions changed {file}')
            f.seek(0); digest=hashlib.sha256()
            while chunk:=f.read(1024*1024):digest.update(chunk)
            if digest.hexdigest()!=row['sha256']:errors.append(f'{n}: SHA-256 mismatch {file}')
    if len(errors)>=20:break
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: 6,344 PNG files, sizes and hashes match {manifest.name}; HTML mirrors and organizer exist.')
