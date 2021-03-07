"""
Get tweets module.
"""
import sys

import tweepy

import auth
import constants
import lib


def get_tweets(api, ids):
    # Only case of one ID for now.

    if False:
        tweets = api.statuses_lookup(ids, tweet_mode="extended")
        # :allowed_param:'id', 'include_entities', 'trim_user', 'map', 'tweet_mode'

        for t in tweets:
            print(t.entities)

        return

    # get media
    tweet = api.get_status(ids[0], tweet_mode="extended")
    import json

    # print(json.dumps(tweet._json, indent=4))
    # print(json.dumps(tweet.entities["media"], indent=4))

    print(json.dumps(tweet.entities["media"][0]["media_url_https"], indent=4))

    # this is optional. but gives more data
    # print(json.dumps(tweet.extended_entities, indent=4))


def main(args):
    api = auth.app_access_token_api()

    ids = [1256704946717822977]
    get_tweets(api, ids)


if __name__ == "__main__":
    main(sys.argv[1:])
