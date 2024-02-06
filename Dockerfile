FROM python:3.12.1-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY .env /app/
COPY . .

CMD [ "python3", "./sitewomen/manage.py", "runserver", "0.0.0.0:8000"]
