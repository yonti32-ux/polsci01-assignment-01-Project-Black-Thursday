@echo off
setlocal
cd /d "%~dp0"
title Black Thursday - Interactive Presentation (polsci01)
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  py -3 "%~dp0launch_presentation.py"
  goto finished
)
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  python "%~dp0launch_presentation.py"
  goto finished
)
echo.
echo Python 3.11 or newer is required for the interactive simulator.
echo Install Python, then double-click this file again.
:finished
if errorlevel 1 (
  echo.
  echo Could not start. See README.md and check whether port 8000 is busy.
)
echo.
pause
