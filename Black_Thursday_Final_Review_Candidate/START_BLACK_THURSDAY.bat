@echo off
setlocal
cd /d "%~dp0"
title Black Thursday - polsci01

where py >nul 2>nul
if not errorlevel 1 (
    py -3 "%~dp0launch_presentation.py"
    goto endrun
)
where python >nul 2>nul
if not errorlevel 1 (
    python "%~dp0launch_presentation.py"
    goto endrun
)

echo ERROR: Could not find Python. Install Python 3.11+ and try again.
exit /b 5

:endrun
set "exitcode=%ERRORLEVEL%"
if not "%exitcode%"=="0" echo Launcher ended with error code %exitcode%.
echo.
pause
exit /b %exitcode%
