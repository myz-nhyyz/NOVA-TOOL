@echo off
setlocal
cd /d "%~dp0"
python -m pip install rich colorama requests selenium webdriver-manager deep-translator twilio phonenumbers geopy aiohttp==3.7.4 pystyle==2.9 fake-useragent==1.2.1 discord.py dnspython pyfiglet
if exist "%~dp0Nova\bot\package.json" (
    cd /d "%~dp0Nova\bot"
    npm install
)
echo.
echo NOVA release setup complete.
pause
