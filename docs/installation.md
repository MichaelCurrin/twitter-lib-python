# Installation


## Dotenv

Create `.env_local` using the template.

Set the values as export variables. Note that this is only for the current process - this is not set at the shell config level, so this is safer.

```sh
export $(< .env_local | xargs)
```

Test

```sh
$ export | grep ACCESS
ACCESS_KEY=foo
ACCESS_SECRET=bar
```
