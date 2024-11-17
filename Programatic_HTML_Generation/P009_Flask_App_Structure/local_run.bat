:: filepath: /d:/Coding/Learn_Web_Development/Programatic_HTML_Generation/P009_Flask_App_Structure/local_run.bat
@echo off
echo ======================================================================
echo Welcome to to the setup. This will setup the local virtual env.
echo And then it will install all the required python libraries.
echo You can rerun this without any issues.
echo ----------------------------------------------------------------------
if exist .env (
    echo Enabling virtual env
) else (
    echo No Virtual env. Please run setup.bat first
    exit /b
)

:: Activate virtual env
call .env\Scripts\activate.bat
set ENV=development
python main.py
deactivate