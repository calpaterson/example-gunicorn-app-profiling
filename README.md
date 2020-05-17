# Example gunicorn app profiling

Inside a virtualenv, run this to install deps:

```
make deps
```

Then to run the app inside the server

```
make run
```

Then visit http://localhost:8000 a couple of times.

Hit ctrl-c.

The profile data is generated - for time inside your application only.  The
avoids cluttering your numbers with stuff about HTTP and gunicorn.

Then run

```
make snakeviz
```

To see what is, AFAIK the state of the art visualiser for Pythonland.
