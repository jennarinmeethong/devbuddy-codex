@echo off
setlocal

for %%I in ("%~dp0..") do set "ROOT=%%~fI"
set "SOURCE=%ROOT%\skill"

if not exist "%SOURCE%\SKILL.md" (
  echo Missing skill\SKILL.md under %ROOT% 1>&2
  exit /b 1
)

if defined CODEX_HOME (
  set "DEST=%CODEX_HOME%\skills\devbuddy"
) else (
  set "DEST=%USERPROFILE%\.codex\skills\devbuddy"
)

if not exist "%DEST%" mkdir "%DEST%"
if errorlevel 1 exit /b 1

robocopy "%SOURCE%" "%DEST%" /MIR /XF .DS_Store /R:2 /W:1 /NFL /NDL /NJH /NJS /NP >nul
if errorlevel 8 (
  echo Failed to install DevBuddy Codex skill to %DEST% 1>&2
  exit /b 1
)

echo Installed DevBuddy Codex skill to %DEST%
echo Start a fresh Codex thread for the skill list to refresh.
exit /b 0
