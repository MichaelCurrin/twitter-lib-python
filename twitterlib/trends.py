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

Each trend item is like this:
    {
        "name": "Milky Way",
        "url": "http://twitter.com/search?q=%22Milky+Way%22",
        "promoted_content": null,
        "query": "%22Milky+Way%22",
        "tweet_volume": null
    }
"""
import json
import sys

import auth

WORLD_OEID = 1


def fetch(woeid):
    """
    Fetch trends items for a target location.

    :param woeid: Where On Earth ID as an integer or integer-like string.
    """
    api = auth.app_access_token_api()

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
    print(json.dumps(trends[:5], indent=4))


if __name__ == "__main__":
    main(sys.argv[1:])
