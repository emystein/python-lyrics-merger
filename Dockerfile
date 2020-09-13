FROM python:3.8

WORKDIR /app

RUN pip install pipenv

COPY . /app/

RUN pipenv install --system --deploy

CMD ["python", "twitter_bot/job_scheduler.py"]
