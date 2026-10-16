
from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_NAME = "Cloud Deployment Lab"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
STUDENT_NAME = os.getenv("STUDENT_NAME", "RINKU")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background: #f3f6fa;
            }}
            .card {{
                background: white;
                max-width: 600px;
                margin: auto;
                padding: 35px;
                border-radius: 12px;
                box-shadow: 0 4px 12px #cccccc;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Cloud Application!</h1>
            <h2>Name: {STUDENT_NAME}</h2>
            <p>Application: {APP_NAME}</p>
            <p>Version: {APP_VERSION}</p>
            <p>Successfully deployed using Docker and AWS EC2.</p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
