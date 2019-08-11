# LyricsMixer
Mix pairs of song lyrics into a new text. It uses [lyricwikia](https://github.com/enricobacis/lyricwikia) to retrieve lyrics from Wikia.

Run tests with `pipenv run pytest`, you can enable console print by running `pipenv run pytest -s`.


# REST API
Run locally with:

```bash
pipenv shell
gunicorn rest_api:app
```


## Endpoints

`HTTP GET http://localhost:8000/`: gives status

`HTTP GET http://localhost:8000/mix/random`: mix two random songs

`HTTP GET http://localhost:8000/mix/artists/<artist1>/<artist2>`: mix random lyrics from two artists

`HTTP GET http://localhost:8000/mix/songs/<artist1>/<title1>/<artist2>/<title2>`: mix two specific lyrics


## Implementation
Implemented using [Flask](https://palletsprojects.com/p/flask/), in file `rest_api.py`


# Twitter Bot
Implemented using [Tweepy](https://www.tweepy.org/).

Environment variables for storing auth tokens:

`LYRICSMIXER_TWITTER_CONSUMER_KEY`

`LYRICSMIXER_TWITTER_CONSUMER_SECRET`

`LYRICSMIXER_TWITTER_ACCESS_TOKEN`

`LYRICSMIXER_TWITTER_ACCESS_TOKEN_SECRET`


# Deployment in Heroku
The file `Procfile` describes both the REST API app and the Twitter bot (as a worker).

Keep awake Heroku instance by running a cron job, every 30 minutes except between 2 am and 8 am, since Heroku force sleep free instances 6 hours a day:

`0/30 0-2,8-23 * * * /usr/bin/curl https://lyricsmixer.herokuapp.com > /tmp/lyricsmixer-ping.log`


# Database setup
Enable PostgreSQL add-on on Heroku dashboard.


Set environment variable `LYRICSMIXER_ENVIRONMENT` to `HEROKU`:

```bash
heroku config:set LYRICSMIXER_ENVIRONMENT=HEROKU
```

Run provisioning script:

```bash
heroku run bash
python database_provision.py
```


Verify:

```bash
heroku pg:info
```

should show 1 table (streamcursor table)
