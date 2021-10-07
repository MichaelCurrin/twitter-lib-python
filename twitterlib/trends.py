"""
Trends module.

Fetch up to 50 trends for a location.

There's only one item in the result and it has data as described below.

Response format:
    {
        "trends": [
            {
                // Trend item.
            },
            {
                // Trend item.
            }
        ]
        "as_of": "2020-10-17T20:28:19Z",
        "created_at": "2020-10-16T00:42:36Z",
        "locations": [
            {
                "name": "Winnipeg",
                "woeid": 2972
            }
        ]
    }

Each trend item is like one of these, where the name is always readable while
the URL and query are URL-encoded:

    Basic:

    {
        "name": "Riverdale",
        "url": "http://twitter.com/search?q=Riverdale",
        "promoted_content": None,
        "query": "Riverdale",
        "tweet_volume": 51000
    }

    Phrase:

    {
        "name": "Milky Way",
        "url": "http://twitter.com/search?q=%22Milky+Way%22",
        "promoted_content": null,
        "query": "%22Milky+Way%22",
        "tweet_volume": null
    }

    Accent:

    {
        "name": "Bélgica",
        "url": "http://twitter.com/search?q=B%C3%A9lgica",
        "promoted_content": None,
        "query": "B%C3%A9lgica",
        "tweet_volume": 17830
    }

    Foreign characters:

    {
        "name": "ワールドカップ",
        "url": "http://twitter.com/search?
            q=%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%82%AB%E3%83%83%E3%83%97",
        "promoted_content": None,
        "query": "%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%82%AB%E3%83%83%E3%83%97",
        "tweet_volume": None
    }

    Hashtag:

    {
        "name": "#FRABEL",
        "url": "http://twitter.com/search?q=%23FRABEL",
        "promoted_content": None,
        "query": "%23FRABEL",
        "tweet_volume": None
    }
"""
import sys

import api_auth

WORLD_OEID = 1


def fetch(woeid):
    """
    Fetch trends items for a target location.

    :param woeid: Where On Earth ID as an integer or integer-like string.
    """
    api = api_auth.app_access_token_api()

    return api.trends_place(woeid)[0]


def main(args):
    """
    Command-line entry-point.

    Accepts an optional argument
        WOEID. e.g. '2972'. Defaults to using Worlwide if not set.
    """
    woeid = int(args.pop(0)) if args else WORLD_OEID

    resp = fetch(woeid)
    trends = resp["trends"]
    for trend in trends:
        out_data = dict(
            name=trend["name"], volume=trend["tweet_volume"], url=trend["url"]
        )
        print(out_data)


if __name__ == "__main__":
    main(sys.argv[1:])
