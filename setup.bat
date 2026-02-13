:: [Windows Device Setup Script]
@echo off

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Install dependencies
echo Installing module dependencies...
pip install -r requirements.txt --upgrade-strategy only-if-needed
echo All dependencies installed.