FROM python:slim
WORKDIR /hivebox
COPY . .
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /var/lib/apt/lists/*
EXPOSE 8000
RUN adduser serveruser
USER serveruser
HEALTHCHECK --interval=1m --start-period=10s --retries=3 CMD [ "curl -f http://localhost:8000/version" ]
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]