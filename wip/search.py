"""
Library search module.

Search for tweets on Twitter.
Future work:
    Refactor with twitter.py script.
    Do app-only only.
    Do retweeting.
    Use cursors.
    Move auth connection setup outside of searching.
    Check types with mypy
See docs:
    https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    http://docs.tweepy.org/en/latest/api.html#API.search
Note the parameters and return values in the Twitter API doc are more reliable
than the tweepy doc.
Attributes and methods on the tweepy Status model.
"""
from dataclasses import dataclass

import lib.auth
from lib import load_conf


CONF = load_conf()
MIN_FAV = MIN_RT = 5


@dataclass
class Tweet:
    guid: int
    created_at: str
    message: str
    favorited: bool
    retweeted: bool
    favorite_count: int
    retweet_count: int
    author_guid: int
    author_screen_name: str

    @property
    def link(self):
        return f"https://twitter.com/{self.author_screen_name}/status/{self.guid}"

    def pretty(self):
        return (
            f"@{self.author_screen_name:20} | {self.created_at.date()} "
            f" | {self.favorite_count} favs | {self.retweet_count} retweets"
            f"\n  {self.message!r}"
        )


def search_api_for_tweets(query, result_type="popular"):
    api = lib.auth.get_api_connection(**CONF["twitter_credentials"])

    tweets = api.search(
        query, count=100, tweet_mode="extended", result_type=result_type
    )

    return tweets


def parse(t):
    return Tweet(
        guid=t.id,
        created_at=t.created_at,
        message=t.full_text,
        author_guid=t.author.id,
        author_screen_name=t.author.screen_name,
        favorited=t.favorited,
        retweeted=t.retweeted,
        favorite_count=t.favorite_count,
        retweet_count=t.retweet_count,
    )


def search(q):
    tweets = search_api_for_tweets(q)
    parsed_tweets = [parse(tweet) for tweet in tweets]

    return parsed_tweets


def top_tweets(tweets, max_tweets=5):
    desired = [
        t
        for t in tweets
        if not t.favorited and (t.retweet_count > MIN_RT or t.favorite_count > MIN_FAV)
    ]
    desired.sort(key=lambda t: -(t.retweet_count + t.favorite_count))
    filtered = desired[:max_tweets]

    return filtered


# Print for now
def fav(tweets):
    for t in tweets:
        parsed = parse(t)
        print(parsed.pretty())
        print(parsed.link)
        # Twitter API buggy
        print(t.favorited)
        # try:
        #     t.favorite()
        # except TweepError as e:
        #     print(e)

        print()


if __name__ == "__main__":
    # TODO move to another script and config
    # Filter excludes messages starting with 'RT'.
    q = '-filter:retweets (biometrics AND innovation) OR ("facial recognition" AND innovation) OR "passwordless security" OR "biometric services" OR (biometric AND blockchain) OR ("IoT" AND innovation)'
    tweets = search_api_for_tweets(q)
    filtered = top_tweets(tweets)
    fav(filtered)

# t = Tweet(1)
