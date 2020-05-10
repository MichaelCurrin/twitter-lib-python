"""
Timeline module.
"""
import sys

import tweepy

# credentials = auth.get_credentials()
# token = auth.app_access_token(**credentials)
# api = auth.setup_api(token)

from auth import TwitterConnection


def get_timeline(api, screen_name=None, user_id=None):
    cursor = tweepy.Cursor(
        api.user_timeline,
        screen_name=screen_name,
        user_id=user_id,
        count=200,
        tweet_mode="extended",
    )

    return cursor


def main(args):
    conn = TwitterConnection()

    conn.set_credentials()
    conn.app_access_token()
    api = conn.setup_api()

    assert len(args) == 1, "Expected screen name"
    screen_name = args.pop(0)
    cursor = get_timeline(api, screen_name=screen_name)
    for i, tweet in enumerate(cursor.items()):
        print(i + 1, tweet.full_text)


if __name__ == "__main__":
    main(sys.argv[1:])
