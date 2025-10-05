#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! 🎉 This is a Python Demo Application running with Flask."

@app.route("/health")
def health():
    return {"status": "UP", "app": "Python Demo App"}

if __name__ == "__main__":
    # Run on http://localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)

