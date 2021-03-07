# Usage


## Set credentials

Do this when opening an terminal, before doing queries. This can be replaced with alternate configs or using `dotenv` in future.

This _can_ be run from inside [twitterlib](/twitterlib/) because of the relative path.

```sh
$ export $(< ../.env_local | xargs)
```


## Get timeline

```sh
$ cd twitterlib
$ # Unbuffered for immediate printing.
$ python -u timeline.py 'realDonaldTrump'
```


From outside this project:

```python
>>> import twitterlib.timeline
>>> cursor = get_timeline(api, screen_name="foo")
>>> for tweet in cursor.items(300):
...     print(tweet.full_text)
```
