"""
Timeline module.
"""
import sys

import tweepy

from . import api_auth, constants, lib


def get_timeline(api, screen_name=None, user_id=None):
    """
    Get tweets of a selected user.
    """
    count = constants.MaxCount.TIMELINE
    tweet_mode = constants.TweetMode.EXTENDED

    cursor = tweepy.Cursor(
        api.user_timeline,
        screen_name=screen_name,
        user_id=user_id,
        count=count.value,
        tweet_mode=tweet_mode.value,
    )

    return cursor


def main(args):
    """
    Command-line entry-point.
    """
    api = api_auth.app_access_token_api()

    assert len(args) == 1, "Expected screen name as an argument"

    screen_name = args.pop(0)

    cursor = get_timeline(api, screen_name=screen_name)
    lib.print_tweets(cursor.items())


if __name__ == "__main__":
    main(sys.argv[1:])
