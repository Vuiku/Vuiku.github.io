@echo off
echo Creating and activating virtual environment...

IF NOT EXIST "venv" (
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
) ELSE (
    call venv\Scripts\activate.bat
)

echo Starting server...
python app.py

pause 