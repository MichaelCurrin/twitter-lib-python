"""
Library module.
"""


def get_message(tweet):
    try:
        message = tweet.full_text
    except AttributeError:
        message = tweet.text

    return message


def print_tweets(cursor):
    for i, tweet in enumerate(cursor.items()):
        print(i + 1, tweet.author.screen_name, get_message(tweet))
