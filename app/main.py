from fastapi import FastAPI

from . import (config)

# main.py is like the conductor that makes sure the app is actually running, connects users to the right endpoints, and delivers the service.

## PURPOSE
# main.py -> is the entry point of the FastAPI application. It is where the app is crated,routes are defined (API endpoints), and manage how application handles requests and responses. It essentially "runs" the application, connecting all parts together.

##HOW IT FITS
# main.py acts as a controller of the application. It takes the settings provided by config.py and uses them to serve requests. It is where the main application logic resides—defining how the app behaves, what routes are available, and how requests are handled.

## MAIN ELEMENTS
# Loading settings - We import the settings from config.py and load them using config.get_settings(). This allows main.py to use the configuration values defined in config.py (e.g., project_name).
settings = config.get_settings()

# Creating FastAPI App
# We create an instance of the FastAPI application using app = FastAPI().This app object is what is used to define routes and serve the application.
app = FastAPI()

# Defining Routes
# @app.get("/") is an API endpoint that serves a response at the root URL (/). In this case, it returns a "hello" message along with the project name from the settings.
@app.get("/")
def read_index():
    return {"hello": "world", "name": settings.project_name}