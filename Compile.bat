echo off

pyinstaller --clean --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --onefile --noconsole Config.py

del /s /q /f Config.spec
rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null