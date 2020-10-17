"""
Locations module.

Get all available locations in the Twitter API.

Each location is like:
    {
        "name": "Worldwide",
        "placeType": {
            "code": 19,
            "name": "Supername"
        },
        "url": "http://where.yahooapis.com/v1/place/1",
        "parentid": 0,
        "country": "",
        "woeid": 1,
        "countryCode": null
    }
"""
import json

import auth


def fetch():
    api = auth.app_access_token_api()

    locations = api.trends_available()

    return locations


def main():
    locations = fetch()

    print(json.dumps(locations, indent=4))


if __name__ == "__main__":
    main()
