#!/bin/sh
set -e

echo "Running KB ingestion..."

python kb_ingestion.py

echo "Starting FastAPI server..."

exec uvicorn app.main:app --host 0.0.0.0 --port 8000