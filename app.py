from http import HTTPStatus

from flask import Flask, redirect, render_template_string, request

from db import initialize_schema, insert_message, list_messages


INDEX_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Message Board</title>
    <style>
      body {
        font-family: sans-serif;
        margin: 2rem auto;
        max-width: 48rem;
        padding: 0 1rem;
      }
      form, li {
        border: 1px solid #d0d7de;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
      }
      label, input, textarea {
        display: block;
        width: 100%;
      }
      input, textarea {
        box-sizing: border-box;
        margin-top: 0.25rem;
        margin-bottom: 0.75rem;
        padding: 0.5rem;
      }
      ul {
        list-style: none;
        padding: 0;
      }
      .meta {
        color: #57606a;
        font-size: 0.9rem;
      }
      .empty {
        color: #57606a;
      }
      .warning {
        background: #fff8c5;
        border: 1px solid #d4a72c;
        border-radius: 0.5rem;
        padding: 0.75rem 1rem;
        margin-bottom: 1rem;
      }
    </style>
  </head>
  <body>
    <h1>Message Board</h1>
    {% if error_message %}
      <p class="warning">{{ error_message }}</p>
    {% endif %}
    <form action="/messages" method="post">
      <label for="name">Name</label>
      <input id="name" name="name" type="text" required>

      <label for="text">Message</label>
      <textarea id="text" name="text" rows="4" required></textarea>

      <button type="submit">Submit</button>
    </form>

    <h2>Messages</h2>
    {% if messages %}
      <ul>
        {% for message in messages %}
          <li>
            <strong>{{ message.name }}</strong>
            <div class="meta">{{ message.created_at.strftime("%Y-%m-%d %H:%M:%S %Z") }}</div>
            <p>{{ message.text }}</p>
          </li>
        {% endfor %}
      </ul>
    {% else %}
      <p class="empty">No messages yet.</p>
    {% endif %}
  </body>
</html>
"""


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SCHEMA_READY"] = False

    def ensure_schema() -> None:
        if not app.config["SCHEMA_READY"]:
            initialize_schema()
            app.config["SCHEMA_READY"] = True

    @app.get("/")
    def index() -> str:
        error_message = None
        messages = []
        try:
            messages = list_messages()
        except Exception:
            error_message = "Message storage is temporarily unavailable. Please try again shortly."
        return render_template_string(
            INDEX_TEMPLATE,
            error_message=error_message,
            messages=messages,
        )

    @app.post("/messages")
    def create_message():
        name = request.form.get("name", "").strip()
        text = request.form.get("text", "").strip()

        if not name or not text:
            return ("Both name and text are required.", HTTPStatus.BAD_REQUEST)

        try:
            ensure_schema()
            insert_message(name=name, text=text)
        except Exception:
            return (
                "Message storage is temporarily unavailable. Please try again shortly.",
                HTTPStatus.SERVICE_UNAVAILABLE,
            )
        return redirect("/", code=HTTPStatus.SEE_OTHER)

    return app


app = create_app()
