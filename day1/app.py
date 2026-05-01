from flask import Flask

app = Flask(__name__)  # Create a Flask application instance


@app.route("/")
def home():
    return "<h1> Day 1 DevOps App </h1><p>Running on ES2 with Nginx + Gunicorn</p>"  # Define a route for the home page that returns an HTML string


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the Flask application on all available interfaces at port 5000


import os
from flask import Flask, request, redirect
from sqlalchemy import create_engine, text

app = Flask(__name__)  # Create a Flask application instance

db_link = os.getenv("DB_LINK")
if not db_link:
    raise RuntimeError("DB_LINK is not set")


@app.route("/")
def home():
    return "<h1> Day 1 and 2 DevOps App </h1><p>Running on ES2 with Nginx + Gunicorn</p>"  # Define a route for the home page that returns an HTML string


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the Flask application on all available interfaces at port 5000