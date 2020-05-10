# Usage


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
