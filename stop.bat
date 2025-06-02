@echo off
echo Stopping server and deactivating virtual environment...

taskkill /F /IM python.exe
call venv\Scripts\deactivate.bat

echo Done!
pause 