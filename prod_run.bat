@ECHO OFF

SET "APP_PORT=8080"
SET "APP_ENV=production"
SET "APP_PATH=%~dp0"
SET "ENV_NAME=fastapi"
SET "RELOAD=NO"
SET "NB_WORKERS=1"

ECHO Application Path
ECHO %APP_PATH%

ECHO Install virtualenv as it will be required to be safe
pip install virtualenv

SET "ENV_PATH=%APP_PATH%\%ENV_NAME%"

ECHO Creating venv locally at %ENV_PATH%
IF NOT EXIST %ENV_PATH% (
    virtualenv %ENV_PATH%
) ELSE (
    ECHO ENV %ENV_PATH% ALREADY EXISTS
)

ECHO Activating the ENV
CALL %ENV_PATH%\Scripts\activate

ECHO Installing dependencies
pip install -r "%APP_PATH%requirements.txt"

ECHO Starting fastapi application
python %APP_PATH%main.py
