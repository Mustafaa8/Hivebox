FROM python:slim
ENV API_VERSION="v0.0.1"
WORKDIR /app
COPY . .
RUN apt update && pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]