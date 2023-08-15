@echo off
if exist venv\ (
	echo Starting Sonos volume controller.
	venv\Scripts\activate
	python ./main.py
) else (
	echo No virtual environment exists. Creating one now, please wait.
	python -m venv venv
	venv\Scripts\activate
	pip install -r requirements.txt
	python ./main.py
)
pause