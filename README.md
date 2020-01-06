# LyricsMixer
Mix pairs of song lyrics into a new text. It uses [lyricwikia](https://github.com/enricobacis/lyricwikia) to retrieve lyrics from Wikia.

Run tests with `pipenv run pytest -v`.

You can enable console print by running `pipenv run pytest -s`.

Code coverage: `pipenv run pytest -v --cov=. --cov-report html`. Then access the coverage report at `htmlcov/index.html`

# REST API
Run locally with:

```bash
pipenv shell
gunicorn lyrics_mixer.rest_api.rest_api_context:app
```


## Endpoints

`HTTP GET http://localhost:8000/`: gives status

`HTTP GET http://localhost:8000/mix/random`: mix two random songs

`HTTP GET http://localhost:8000/mix/artists/<artist1>/<artist2>`: mix random lyrics from two artists

`HTTP GET http://localhost:8000/mix/songs/<artist1>/<title1>/<artist2>/<title2>`: mix two specific lyrics


## Implementation
Implemented using [Flask](https://palletsprojects.com/p/flask/), in directory `lyrics_mixer/rest_api` 


# Twitter Bot
Implemented using [Tweepy](https://www.tweepy.org/).

Environment variables for storing auth tokens:

`TWITTER_CONSUMER_KEY`

`TWITTER_CONSUMER_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_TOKEN_SECRET`


# Deployment in Heroku
The file `Procfile` describes both the REST API app and the Twitter bot (as a worker).

## Keep awake Heroku instance
Keep awake Heroku instance by running a schedule job.

### Cron
Every 30 minutes except between 2 am and 8 am, since Heroku force sleep free instances 6 hours a day:

`0/30 0-2,8-23 * * * /usr/bin/curl https://lyricsmixer.herokuapp.com > /tmp/lyricsmixer-ping.log`

### Systemd Timer
Install unit provided in the `lyrics_mixer/setup` directory: `heroku_lyricsmixer_ping.timer`, `heroku_lyricsmixer_ping.service`

```bash
cd lyrics_mixer/setup
sudo cp heroku_lyricsmixer_ping.* /etc/systemd/system
sudo systemctl enable heroku_lyricsmixer_ping.timer
sudo systemctl start heroku_lyricsmixer_ping.service
```

Check timer is installed:

```bash
sudo systemctl list-timers --all
```

## Database setup
Enable PostgreSQL add-on on Heroku dashboard.

Run provisioning script:

```bash
heroku run bash
python lyrics_mixer/setup/database_provision.py
```

Verify:

```bash
heroku pg:info
```

should show 1 table (streamcursor table)
