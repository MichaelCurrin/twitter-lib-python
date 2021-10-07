# Configuration


## Dotenv

### 1. Create values

Create a local dotenv file using the template.

```sh
$ cp .env.template.local .env.local
```

Update `.env.local` with your Twitter credentials. Never share those details publicly.

Note this `.env.local` is ignored by Git and is also separate from the versioned `.env` file which has been set up for VS Code.

### 2. Read values

Set the values as export variables whenever you need to use the details.

The command below is provided for macOS and Linux only. Be sure to run from the repo root, otherwise you'll see very noise output.

```sh
$ export $(< .env.local | xargs)
```

Note that this is only for the current process - this is not set at the shell config level, so this is safer.

There is also a `dotenv` Python package which can read this within the code, but this is not covered here.

### 3. Check

Test that values are set in environment:

```console
$ export | grep ACCESS
ACCESS_KEY=foo
ACCESS_SECRET=bar
```
