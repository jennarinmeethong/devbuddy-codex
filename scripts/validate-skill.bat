@echo off
setlocal

for %%I in ("%~dp0..") do set "ROOT=%%~fI"

where py >nul 2>nul
if not errorlevel 1 (
  py -3 "%ROOT%\scripts\validate-skill.py"
  exit /b
)

where python >nul 2>nul
if not errorlevel 1 (
  python "%ROOT%\scripts\validate-skill.py"
  exit /b
)

where python3 >nul 2>nul
if not errorlevel 1 (
  python3 "%ROOT%\scripts\validate-skill.py"
  exit /b
)

echo Python 3 is required to validate the skill. 1>&2
exit /b 1
