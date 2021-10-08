"""
API Authorization module.

Manage Twitter credentials, authentication, and an API connection.

This module can't be named `api` or `auth` otherwise it clashes with variables in
other modules.
"""
import os
from typing import Optional

import tweepy
from tweepy.api import API
from tweepy.auth import OAuthHandler
from typing_extensions import TypedDict


CONNECTION_OPTIONS = dict(
    wait_on_rate_limit=True,
    retry_count=3,
    retry_delay=5,
    retry_errors=[401, 404, 500, 503],
)

Credentials = TypedDict(
    "Credentials",
    {
        "consumer_key": str,
        "consumer_secret": str,
        "access_key": Optional[str],
        "access_secret": Optional[str],
    },
)


def get_credentials(use_access_tokens: bool):
    """
    Read Twitter API credentials from environment variables.
    """
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")

    assert consumer_key and consumer_secret, "Consumers tokens must always be set"

    if use_access_tokens:
        access_key = os.environ.get("ACCESS_KEY")
        access_secret = os.environ.get("ACCESS_SECRET")

        assert access_key and access_secret, "Access tokens must be set for chosen flow"

    credentials: Credentials = {
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret,
        "access_key": access_key,
        "access_secret": access_secret,
    }

    return credentials


def setup_auth(use_access_tokens: bool) -> OAuthHandler:
    """
    Return configured Tweepy auth handler.
    """
    credentials = get_credentials(use_access_tokens)

    auth = tweepy.OAuthHandler(
        credentials["consumer_key"], credentials["consumer_secret"]
    )
    if use_access_tokens:
        auth.set_access_token(credentials["access_key"], credentials["access_secret"])

    return auth


def setup_api(auth: OAuthHandler) -> API:
    """
    Get Tweepy API connection object using authentication details.
    """
    return tweepy.API(auth, **CONNECTION_OPTIONS)


def app_access_token_api() -> API:
    """
    Get API object which has App Access Token auth.
    """
    auth = setup_auth(use_access_tokens=True)

    return setup_api(auth)


def main():
    """
    Command-line entry point to test API access.
    """
    api = app_access_token_api()
    print(api.verify_credentials())


if __name__ == "__main__":
    main()
