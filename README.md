# Task Tracking Portal

This is a Django-based Task Tracking Portal application. This README provides instructions on how to set up and run the application both using Docker and directly on your local machine.

## Prerequisites

- Python 3.10 or later installed.
- Pip installed.
- currently  sqlite3 running , MySQL database server running optional, dialect can be changed to  .

## Running the application


### From Image

    pull the the following image, 

    $ docker pull giv462/task-track

    to run 

    docker run -d -p 8000:8000  giv462/task-track:dev

    docker run -d -p 8000:8000  giv462/task-track:latest     <stable>

### Local setup

    django setup: https://docs.djangoproject.com/en/5.0/

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

## Configuration

### Configure the Database

Update the `settings.py` file to configure the external MySQL database:

# settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",      # Replace with your database name
        "USER": "",      # Replace with your database user
        "PASSWORD": "",  # Replace with your database password
        "HOST": "",      # Replace with your database host
        "PORT": "",      # Replace with your database port
    }
}


