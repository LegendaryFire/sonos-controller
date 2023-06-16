@echo off
if exists venv\ (
	echo Starting Sonos volume controller.
) else (
	echo No virtual environment exists. Creating one now.
	python ./main.py
)
pause