
FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY src /app/src
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
