# Usage

As per [Installation](installation.md) doc, activate the virtual environment and load the config file before running these commands.

```sh
$ source venv/bin/activate
$ export $(< .env.local | xargs)
```


## CLI

### Get tweets of a Twitter user

Note use of unbuffered flag for immediate printing.

```sh
$ cd twitterlib
$ python -u timeline.py 'realDonaldTrump'
```


## Python package API

### Get tweets of a Twitter user

Use the library in your own project. TODO: Make this an installable package.

- `main.py`
    ```python
    import twitterlib.timeline


    cursor = get_timeline(api, screen_name="foo")

    for tweet in cursor.items(300):
        print(tweet.full_text)
    ```
