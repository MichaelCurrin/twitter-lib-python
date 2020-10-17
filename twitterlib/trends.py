"""
Trends module.

Fetch up to 50 trends for a location.

There's only one item in the result and it has data as described below.

Response format:
    {
        "trends": [
            {},
            {}
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

Each trend is like this:
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


def fetch(woeid):
    """
    Accepts an integer or an integer-like string.
    """
    api = auth.app_access_token_api()

    return api.trends_place(woeid)[0]


def main(args):
    """
    Optional argument - WOEID. e.g. '2972'. Defaults to using Worlwide if not set.
    """
    if args:
        woeid = int(args.pop(0))
    else:
        woeid = 1

    trends = fetch(woeid)["trends"]
    print(json.dumps(trends[0], indent=4))


if __name__ == "__main__":
    main(sys.argv[1:])
