# Installation


## Dotenv

### Setup

Create `.env_local` using the template.

Set the values as export variables. Note that this is only for the current process - this is not set at the shell config level, so this is safer.

### Test

Run this from the root of the project:

```sh
$ export $(< .env_local | xargs)
```

If there was an _error_ in the subshell command in brackets, then the `export` command will run alone and you'll see a lot of output.

Check values:

```sh
$ export | grep ACCESS
ACCESS_KEY=foo
ACCESS_SECRET=bar
```
