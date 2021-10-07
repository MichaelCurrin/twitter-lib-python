"""
Search module.
"""
import sys

import tweepy

import auth
import constants
import lib


def geo_to_str(latitude, longitude, distance):
    """
    Return geolocation data as string of comma-separated values.
    """
    has_valid_unit = distance.endswith("km") or distance.endswith("mi")
    assert has_valid_unit, "Must include units as 'km' or 'mi'."

    return ",".join((latitude, longitude, distance))


def search(api, q=None, geocode=None, lang=None):
    """
    Get tweets using search parameters.
    """
    count = constants.MaxCount.SEARCH_TWEETS
    result_type = constants.ResultType.MIXED
    tweet_mode = constants.TweetMode.EXTENDED

    assert (
        q or geocode or lang
    ), "At least one of the optional arguments in `search` function must be set"

    cursor = tweepy.Cursor(
        api.search,
        q=q,
        geocode=geocode,
        lang=lang,
        count=count.value,
        result_type=result_type.value,
        tweet_mode=tweet_mode.value,
    )

    return cursor


def main(_args):
    """
    Command-line argument.
    """
    api = auth.app_access_token_api()

    geocode = geo_to_str("33.3125", "44.3661", "100km")
    lang = "ar"

    cursor = search(api, geocode=geocode, lang=lang)

    tweets = list(lib.print_tweets(cursor.items(50)))
    lib.tweets_to_csv(tweets)


if __name__ == "__main__":
    main(sys.argv[1:])
