"""
Library module.
"""
import csv


def get_message(tweet):
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
        yield tweet


def write_csv(filepath, rows):
    """
    Note this will overwrite and not append.
    """
    with open(filepath, "w") as f_out:
        writer = csv.writer(f_out)
        writer.writerows(rows)


def tweets_to_csv(tweets):
    out_file = "var/tweets.csv"

    out_tweets = [
        (tweet.id, tweet.author.screen_name, get_message(tweet)) for tweet in tweets
    ]
    write_csv(out_file, out_tweets)
