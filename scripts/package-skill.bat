@echo off
setlocal

for %%I in ("%~dp0..") do set "ROOT=%%~fI"
set "DIST=%ROOT%\dist"
set "ZIP=%DIST%\devbuddy-codex-skill.zip"
set "TEMP_ROOT=%TEMP%\devbuddy-codex-%RANDOM%-%RANDOM%"

if not exist "%ROOT%\skill\SKILL.md" (
  echo Missing skill\SKILL.md under %ROOT% 1>&2
  exit /b 1
)

if not exist "%DIST%" mkdir "%DIST%"
if errorlevel 1 exit /b 1

if exist "%ZIP%" del /f /q "%ZIP%"
if errorlevel 1 exit /b 1

mkdir "%TEMP_ROOT%\devbuddy"
if errorlevel 1 exit /b 1

robocopy "%ROOT%\skill" "%TEMP_ROOT%\devbuddy" /E /XF .DS_Store /R:2 /W:1 /NFL /NDL /NJH /NJS /NP >nul
if errorlevel 8 (
  echo Failed to stage the skill for packaging. 1>&2
  rmdir /s /q "%TEMP_ROOT%"
  exit /b 1
)

powershell.exe -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -Command "Compress-Archive -LiteralPath '%TEMP_ROOT%\devbuddy' -DestinationPath '%ZIP%' -CompressionLevel Optimal -Force"
set "RESULT=%errorlevel%"

rmdir /s /q "%TEMP_ROOT%"

if not "%RESULT%"=="0" (
  echo Failed to create %ZIP% 1>&2
  exit /b %RESULT%
)

echo Created %ZIP%
exit /b 0
