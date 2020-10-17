# Installation


## Dotenv

### Create and update

Create a local dotenv file using the template.

```sh
$ cp .env.template.local .env.local
```

Update it with your Twitter credentials. Never share those details publically.

### Read values

Set the values as export variables whenever you need to use the details.

The command below is provided for macOS and Linux only.

```sh
$ export $(< .env.local | xargs)
```

Note that this is only for the current process - this is not set at the shell config level, so this is safer.

### Check

Test that values are set in environment:

```sh
$ export | grep ACCESS
ACCESS_KEY=foo
ACCESS_SECRET=bar
```
