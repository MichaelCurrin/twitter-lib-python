# Usage

As per [Installation](installation.md) doc, activate the virtual environment before running these commands.
`
```sh
$ source venv/bin/activate
```


## CLI

Note use of unbuffered `-u` flag in some cases for immediate printing.

### Validate credentials

```sh
$ make auth
```

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

TODO: Make this an installable package.

Use the library in your own project.

Load config details:

```sh
$ export $(< .env.local | xargs)
```

Set up a script.

- `main.py`
    ```python
    import twitterlib.timeline
    from twitterlib import api_auth
s

    api = api_auth.app_access_token_api()

    cursor = twitterlib.timeline.get_timeline(api, screen_name="BarackObama")

    for tweet in cursor.items(300):
        print(tweet.full_text)
    ```

Run it:

```
$ python main.py
```
