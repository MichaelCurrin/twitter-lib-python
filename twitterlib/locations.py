"""
Locations module.

Get all available locations in the Twitter API.

Sample usage - write the prettified output to a JSON file.
    python locations.py > var/locations.json

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

from . import api_auth


def fetch():
    """
    Return locations that the API makes trends available fors.
    """
    api = api_auth.app_access_token_api()

    locations = api.available_trends()

    return locations


def main():
    """
    Command-line entry-point.
    """
    locations = fetch()

    print(json.dumps(locations, indent=4))


if __name__ == "__main__":
    main()
