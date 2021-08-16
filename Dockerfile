FROM python:3.9-slim

WORKDIR /app

RUN pip install pipenv

COPY . /app/

RUN pipenv install --system --deploy

CMD ["python", "twitter_bot.py"]
