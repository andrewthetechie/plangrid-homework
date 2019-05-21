# plangrid-homework
Homework problem for plangrid DevOps/SRE. I approached the problem using Python and Flask.

My solution is a Flask application designed to be run on Python 3.6/7 behind gunicorn. 
If I were deploying this in production, I would put gunicorn behind a reverse proxy (nginx, caddy, haproxy).

## Files
* app.py -- The main flask app. Has routes and app init methods in the same file. For a larger app, I would have split these routes into blueprints but tried to keep complexity down here
* config.py -- a quick config class to configure the app. Split out so the app could be easier expanded
* test_app.py -- tests for app.py
* Dockerfile -- dockerfile for running the app
* Test-Dockerfile -- dockerfile for running tests on this app


# Requirements
This application is dockerized for ease of use. Docker provides instructions on configuring docker here: https://docs.docker.com/v17.12/install/
It also uses `make` to make working with the app easier. If you do not have make installed, you can install it or use the provided manual commands.
 

# Setup

To build this container, from the root of the repo run:

    make build
    
This will build a container to your local system named "aherrington-plangrid-homework". 

You can also do this manually with:
    
    docker build -t aherrington-plangrid-homework .
    
# Running the application

The application can be run with default settings:
   
    make run
    
To do this manually without make:

    docker run -it -p 8000:8000 aherrington-plangrid-homework

## Debug Mode 
To enable the app in debug mode and get debug logs (including requests logs) you can use:

    make run-debug
    
or

    docker run -it -p 8000:8000 --env LOGLEVEL=DEBUG aherrington-plangrid-homework
    
# Testing

Testing also uses a docker container. To build it:

    make build-test
    
Or manually:

    docker build -f Test-Dockerfile -t aherrington-plangrid-homework-test .
    
To run the tests:

    make test
    
Or:

    docker run -it aherrington-plangrid-homework-test
    
## Function testing the application
A script using curl has been provided to test the application at test_with_curl.sh. Make it executable on your system (chmod +x) and run it

    ./test_with_curl.sh
    Testing HTML Output with a get
    <p>Hello, World</p>Testing JSON Output with a get
    {"message":"Good morning"}
    Testing HTML Output with a post
    <p>Hello, World</p>Testing JSON Output with a post
    {"message":"Good morning"}

