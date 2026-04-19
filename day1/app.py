from flask import Flask

app = Flask(__name__)  # Create a Flask application instance


@app.route("/")
def home():
    return "<h1> Day 1 DevOps App </h1><p>Running on ES2 with Nginx + Gunicorn</p>"  # Define a route for the home page that returns an HTML string


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the Flask application on all available interfaces at port 5000