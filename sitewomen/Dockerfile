FROM python:3.12.1-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

COPY . .

ENV APP_NAME=SITEWOMEN

RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
