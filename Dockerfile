# FROM python:3.8-alpine
FROM python:3.8-slim

WORKDIR /app

# fix "Error: pg_config executable not found." when using Alpine
# RUN apk add gcc musl-dev python3-dev postgresql-dev 

RUN pip install pipenv

COPY . /app/

RUN pipenv install --system --deploy

CMD ["python", "twitter_bot.py"]
