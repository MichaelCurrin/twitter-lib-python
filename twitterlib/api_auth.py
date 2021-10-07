"""
API Authorization module.

This can't be named `api` or `auth` otherwise it clashes with variables in
other modules.
"""
import os

import tweepy


CONNECTION_OPTIONS = dict(
    wait_on_rate_limit=True,
    retry_count=3,
    retry_delay=5,
    retry_errors=[401, 404, 500, 503],
)


def get_credentials_from_env():
    """
    Read Twitter API credentials from environment variables.
    """
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")

    access_key = os.environ.get("ACCESS_KEY")
    access_secret = os.environ.get("ACCESS_SECRET")

    return consumer_key, consumer_secret, access_key, access_secret


class TwitterConnection:
    """
    Manage Twitter credentials, authentication and making a tweepy.API object.
    """

    def __init__(self):
        self.auth = None

        self.consumer_key = None
        self.consumer_secret = None
        self.access_key = None
        self.access_secret = None

    def validate_consumer_creds(self):
        assert self.consumer_key, "Consumer key must be set"
        assert self.consumer_secret, "Consumer secret must be set"

    def validate_access_creds(self):
        assert self.access_key, "Access key must be set"
        assert self.access_secret, "Access secret must be set"

    def set_credentials(self):
        """
        Read credentials and set them on the instance.
        """
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

        self.validate_consumer_creds()

    def app_access_token(self):
        """
        Return API object authorized with App Access Token.
        """
        self.validate_access_creds()

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)

        return self.auth

    def app_only_token(self):
        """
        Return API connection using App Only Token approach.
        """
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)

        return self.auth

    def setup_api(self):
        return tweepy.API(self.auth, **CONNECTION_OPTIONS)


def app_access_token_api():
    """
    Wrapper to get API object which has App Access Token auth.

    TODO Refactor the class to a function only since using this
    function seems to be the main entry-point.
    """
    conn = TwitterConnection()
    conn.set_credentials()
    conn.app_access_token()

    api = conn.setup_api()

    return api


def test():
    api = app_access_token_api()
    print(api.verify_credentials())


if __name__ == "__main__":
    test()
