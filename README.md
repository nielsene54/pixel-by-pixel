# The most over engineered solution to rendering a picture

This repo is my crack at making the most over engineered solution to
rendering an image I could think of.

It consists of a frontend and a backend that need to run on separate servers.

## Implementation
The front end calls the backend once for every pixel it needs to render.

## Prerequisites
* Python 3.4 and above
* [virtualenv](https://virtualenv.pypa.io/en/stable/)

## Running instructions
It is assumed you are running all commands from the root of this repo and using bash.

### Backend
First cd into the `backend` directory

    cd backend

Create a virtual env there

    virtualenv venv -p python3

Activate the virtualenv

    . venv/bin/activate

Install pip requirements

    pip install -r requirements.txt

Run the server

    python backend.py

### Frontend
cd into the `frontend` directory

    cd frontend

Run a simple python server

    python -m SimpleHTTPServer 8001

Navigate to http://localhost:8001/pixel-by-pixel.html and watch it take forever to load.

# Addendum

Feel free to expand on this and make it even worse!
