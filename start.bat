@echo off
setlocal
cd /d "%~dp0"
title NOVA-TOOL v1.0
python "%~dp0Nova\main.py"
if errorlevel 1 pause
