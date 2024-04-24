FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app
RUN pip --no-cache-dir install -r requirements.txt

ENTRYPOINT ["python", "placeholder_service.py"]
