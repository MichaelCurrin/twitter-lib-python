# TODO resolve conflict where this is auth.py and auth is the typical name for an object within.
import tweepy

import os


def get_credentials():
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")

    access_key = os.environ.get("ACCESS_KEY")
    access_secret = os.environ.get("ACCESS_SECRET")

    return dict(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_key=access_key,
        access_secret=access_secret,
    )


# Or get these internally or add a wrapper. TBD on structure.
def app_access_token(consumer_key, consumer_secret, access_key, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_key, access_secret)

    return auth


def app_only_token(consumer_key, consumer_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    return auth


def setup_api(auth):
    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        retry_count=3,
        retry_delay=5,
        retry_errors=[401, 404, 500, 503],
    )

    return api
