# TODO resolve conflict where this is auth.py and auth is the typical name for an object within.
import tweepy

import os


def get_credentials_from_env():
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")

    access_key = os.environ.get("ACCESS_KEY")
    access_secret = os.environ.get("ACCESS_SECRET")

    return consumer_key, consumer_secret, access_key, access_secret


class TwitterConnection:
    def __init__(self):
        # Avoid moving setup steps here until I know the flows.
        # Maybe there are methods here or functions outside for one line setup
        # flows.
        self.auth = None

        self.consumer_key = None
        self.consumer_secret = None
        self.access_key = None
        self.access_secret = None

        self.connection_options = dict(
            wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True,
            retry_count=3,
            retry_delay=5,
            retry_errors=[401, 404, 500, 503],
        )

        self.api = None

    def set_credentials(self):
        (
            consumer_key,
            consumer_secret,
            access_key,
            access_secret,
        ) = get_credentials_from_env()

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_key = access_key
        self.access_secret = access_secret

    def app_access_token(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)

        return self.auth

    def app_only_token(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)

        return self.auth

    def setup_api(self):
        self.api = tweepy.API(self.auth, **self.connection_options)

        return self.api


def test():
    conn = TwitterConnection()

    conn.set_credentials()
    conn.app_access_token()
    api = conn.setup_api()

    print(api.verify_credentials())


if __name__ == "__main__":
    test()
