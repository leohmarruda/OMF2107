@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File project\scripts\run-story-meshy.ps1
if errorlevel 1 pause
