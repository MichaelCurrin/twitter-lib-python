# Usage

Activate the virtual environment before running these commands.


## Get Tweet timeline

```sh
$ cd twitterlib
$ # Not unbuffered for immediate printing.
$ python -u timeline.py 'realDonaldTrump'
```

Use the library in your own project. TODO: Make this an installable package.

- `main.py`
    ```python
    import twitterlib.timeline


    cursor = get_timeline(api, screen_name="foo")

    for tweet in cursor.items(300):
    print(tweet.full_text)
    ```
