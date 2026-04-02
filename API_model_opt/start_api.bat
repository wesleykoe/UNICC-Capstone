@echo off
cd /d C:\Users\DELL\Desktop\unicc-council-api

echo Starting FastAPI server...
start "UNICC API" cmd /k "conda run --no-capture-output -n unicc python -m uvicorn app:app --host 127.0.0.1 --port 8000"

timeout /t 5 /nobreak > nul

echo Starting ngrok tunnel...
start "ngrok" cmd /k "ngrok http 8000"

timeout /t 3 /nobreak > nul

start http://127.0.0.1:8000/docs
