FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# OpenEnv expects the server to run on port 8000
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]