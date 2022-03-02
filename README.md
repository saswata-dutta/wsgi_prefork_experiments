# Motivation

Gunicorn pre forks py workers.
To save on memory we can pre-load and use copy on write of certain data-structs on the forked children;
Some data-structs might not be fork-safe (due to stateful locks, file descriptors), so initialized post fork.

### Try it out

`cd wsgi_prefork_experiments; gunicorn sample:app; cd ..`

`curl -X POST --connect-timeout 5 http://127.0.0.1:8000/invocations`

`curl -X GET http://127.0.0.1:8000/ping`
