# flask-docker
Template for simple Flask app, ready to deploy on Docker

# Sources

This template was built based on the following sources:

[Miguel Grinberg's Flask Mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
[Flask documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/):

# Directory structure

```
flask-docker
|   .env
|   .gitignore
|   boot.sh
|   config.py
|   docker-compose.yml
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
    +---templates
    |       index.html
    |
    \---tests
            apitest.py
```

## Files explained

### `.env`

Environment variables used by Flask. 

- Do not upload this to GitHub if cloning / forking this repository as it contains sensitive variables like the secret key. Include in the .gitignore file!
- For local development, the environment variables in this file can be automatically loaded by installing the `python-dotenv` package.
- If using Docker, the environment variables can be passed to Docker when running the container with the `docker run [...] --env-file=.env` parameter

The important variables contained in the file are:

- `FLASK_APP=flaskexampleapp`: instructs Flask which application to run when calling `flask run`
- `FLASK_ENV=development`: sets Flask to development mode with full debugging
- `SECRET_KEY=secret_key`: the secret key used by the WTForms module against CSRF attacks. Don't publish this key!

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