FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install awscli -y

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]