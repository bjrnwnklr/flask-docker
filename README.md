# flask-docker
Template for simple Flask app, ready to deploy on Docker

# Build and run

Build and run the Docker container with the following commands:

```shell
$ docker build --tag flask-docker-example .
$ docker run --name flask --detach --publish 8000:5000 --env-file=.env --rm flask-docker-example
```

# Error messages

If you receive the following error message when running the Docker container:

`standard_init_linux.go:219: exec user process caused: no such file or directory`

Change the CRLF in VSCode to LF and save the `boot.sh` file with a Unix line ending.