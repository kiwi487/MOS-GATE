@echo off
setlocal
cd /d "%~dp0"
echo MOS COMSOL: Install images
set "IMAGE_SOURCE=%~dp0Image.zip"
if not "%~1"=="" set "IMAGE_SOURCE=%~1"
if not exist "%IMAGE_SOURCE%" if exist "%~dp0Image" set "IMAGE_SOURCE=%~dp0Image"
if not exist "%IMAGE_SOURCE%" (
  echo [ERROR] Image.zip or extracted Image directory not found.
  echo Copy Image.zip beside this BAT or drag your ZIP onto it.
  pause
  exit /b 2
)
where py >nul 2>&1
if not errorlevel 1 (
  py -3 "%~dp0organize_images.py" --source "%IMAGE_SOURCE%"
) else (
  python "%~dp0organize_images.py" --source "%IMAGE_SOURCE%"
)
set "RESULT=%errorlevel%"
if not "%RESULT%"=="0" echo [FAILED] Check the error details above.
if "%RESULT%"=="0" echo [DONE] Install images completed successfully.
pause
exit /b %RESULT%
