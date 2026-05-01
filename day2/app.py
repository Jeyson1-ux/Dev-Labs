import os
from flask import Flask, request, redirect
from sqlalchemy import create_engine, text

app = Flask(__name__)

DB_LINK = os.getenv("DB_LINK")

if not DB_LINK:
    raise RuntimeError("DB_LINK environment variable is not set")

engine = create_engine(DB_LINK, future=True)


def init_db():
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as conn:
        conn.execute(text(query))


init_db()


@app.route("/")
def home():
    return """
    <h1>Day 2 DevOps App</h1>
    <p>Now running on PostgreSQL</p>

    <form method="POST" action="/signup">
        <input name="username" placeholder="Enter username" required>
        <button type="submit">Create user</button>
    </form>

    <p><a href="/users">View Users</a></p>
    """


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username", "").strip()

    if not username:
        return "The username is required", 400

    query = """
    INSERT INTO users (username)
    VALUES (:username)
    ON CONFLICT (username) DO NOTHING;
    """

    with engine.begin() as conn:
        conn.execute(text(query), {"username": username})

    return redirect("/users")


@app.route("/users")
def users():
    query = """
    SELECT username, created_at
    FROM users
    ORDER BY id DESC;
    """

    with engine.connect() as conn:
        rows = conn.execute(text(query)).fetchall()

    output = "<h2>Users</h2><ul>"

    for row in rows:
        output += f"<li>{row.username} - {row.created_at}</li>"

    output += "</ul><p><a href='/'>Go Back</a></p>"

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)