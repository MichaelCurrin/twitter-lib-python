import tweepy


# TODO Create logic to handle inner config values, requesting
# token type and reading credentials.
def get_api_connection(
    consumer_key, consumer_secret, access_key=None, access_secret=None
):
    """
    Authorize with Twitter and return API connection object.

    If access credentials are provided, then App Access Token is generated,
    with user context for the authenticating user. e.g. get my timeline
    or tweet as me.

    If not, then an Application-Only Token is generated, which has no user
    context but can still perform get actions like search tweets or lookup
    target user. Note streaming is does not worth with this.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    if access_key and access_secret:
        auth.set_access_token(access_key, access_secret)

    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        retry_count=3,
        retry_delay=5,
        retry_errors=[401, 404, 500, 503],
    )

    return api


# TODO
# def test_connection


# if __name__ == '__main__':
