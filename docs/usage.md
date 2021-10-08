# Usage

As per [Installation](installation.md) doc, activate the virtual environment and load the config file before running these commands.

```sh
$ source venv/bin/activate
$ export $(< .env.local | xargs)
```


## CLI

Note use of unbuffered `-u` flag in some cases for immediate printing.

### Get tweets of a Twitter user

Using the default.

```sh
$ make timeline
```

Specify a username.

```sh
$ make demo-timeline screen_name=BarackObama
```

### Trends

```sh
$ make trends
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
