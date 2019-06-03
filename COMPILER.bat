@echo off
:: Variables
set filename="osukeyboard"

:: Make it compile beautifuldiscord to an executable file
pyinstaller index.py --onefile --icon=logo.ico --add-data="sounds/*.mp3;sounds" --name %filename%.exe

:: Copy compiled file to root
del %filename%.exe
copy dist\%filename%.exe .
