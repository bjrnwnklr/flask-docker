# flask-docker
Template for simple Flask app, ready to deploy on Docker

# Sources

This template was heavily influenced by the following sources:

[Miguel Grinberg's Flask Mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
[Flask documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/):

# Directory structure

```
flask-docker
|   .env
|   .gitignore
|   boot.sh
|   config.py
|   docker-requirements.txt
|   Dockerfile
|   LICENSE
|   MANIFEST.in
|   README.md
|   requirements.txt
|   setup.py
|       
\---flaskexampleapp
    |   forms.py
    |   routes.py
    |   __init__.py
    |   
    +---static
    |       style.css
    |       
    \---templates
            index.html
```

## Files explained

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