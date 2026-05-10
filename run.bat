@echo off
echo ================================================
echo   Voice Music Agent
echo ================================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Download from https://python.org
    pause
    exit /b 1
)

:: Install dependencies silently if needed
echo Checking dependencies...
pip install -r requirements.txt -q

echo.
echo Starting in system tray...
echo The agent will appear in your taskbar (bottom-right).
echo You can close this window after — the agent keeps running.
echo.

:: pythonw = launches Python with no console window
start "" pythonw src\tray_app.py
