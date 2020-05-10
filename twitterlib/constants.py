"""
Constants module.
"""
from enum import Enum


class MAX_COUNT(Enum):
    """
    The maximum count value allowed for an method/endpoint.
    """

    SEARCH_TWEETS = 100
    TIMELINE = 200


class TweetMode(Enum):
    """
    Options for requesting short or long tweet messages.

    For normal, you get possibly truncated message - use `tweet.text`.
    for extended, you ge anr expanded message - use `tweet.full_text`.
    """

    NORMAL = "normal"
    EXTENDED = "extended"


class ResultType(Enum):
    """
    Options for searching for tweets.
    """

    MIXED = "mixed"
    RECENT = "recent"
    POPULAR = "popular"
