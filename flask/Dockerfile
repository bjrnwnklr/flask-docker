FROM python:3.9-slim-buster

# create user so we don't run as root, then change into the homedir of the user and switch to the user
# The rest of the dockerfile will now be run under this user.
RUN adduser --disabled-login flask-docker
WORKDIR /home/flask-docker
USER flask-docker

# create a virtual environment and install the requirements into it
# gunicorn is installed separately as it is not in the local requirements file. We only need it on Docker.
COPY requirements.txt requirements.txt
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt
RUN .venv/bin/pip install gunicorn

# Copy the app code and make the boot.sh script executable
COPY flaskexampleapp flaskexampleapp
COPY config.py setup.py boot.sh ./

# Expose port 5000 (standard Flask port) and run boot.sh (which activates the virtual environment and runs gunicorn)
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]