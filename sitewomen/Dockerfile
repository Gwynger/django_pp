FROM python:3.12.1-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

COPY . .

ENV APP_NAME=SITEWOMEN

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

CMD gunicorn sitewomen.wsgi:application -b 0.0.0.0:8000
