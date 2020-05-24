@echo off

call set_up_google_app_credentials.bat

cd F:\Facultate Anul 4\LucrareLicenta\ChatLearner-master\ChatLearner-master
call setup_pythonpath_env_variable.bat

call venv_py35\Scripts\activate

cd chatbot
python botui.py
