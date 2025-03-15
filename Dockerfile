FROM python:slim
WORKDIR /hivebox
COPY . .
RUN apt-get update && pip install --no-cache-dir -r requirements.txt && rm -rf /var/lib/apt/lists/*
EXPOSE 8000
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]