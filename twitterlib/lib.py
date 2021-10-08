"""
Library module.
"""
import csv
from pathlib import Path


TWEETS_CSV_PATH = Path(__file__).parent / "var" / "tweets.csv"


def get_message(tweet):
    """
    Get the message attribute on a Tweet object.

    The attribute available depends on the parameters on the query to Twitter.
    """
    try:
        message = tweet.full_text
    except AttributeError:
        message = tweet.text

    return message


def print_tweets(tweets):
    """
    Iterate over tweets, printing them and returning each tweet.

    Tweets can be from a standard query or a paged cursor items query.
    This does not support cursor.page option.
    """
    for i, tweet in enumerate(tweets):
        print(i + 1, tweet.id, tweet.author.screen_name, get_message(tweet))


def write_csv(filepath, rows):
    """
    Note this will overwrite and not append.
    """
    print(f"Writing to {filepath}")

    with open(filepath, "w", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerows(rows)


def tweets_to_csv(tweets, out_path=None):
    """
    Write out tweets to a CSV file.
    """
    if not out_path:
        out_path = TWEETS_CSV_PATH

    out_tweets = [
        (tweet.id, tweet.author.screen_name, get_message(tweet)) for tweet in tweets
    ]
    write_csv(out_path, out_tweets)
