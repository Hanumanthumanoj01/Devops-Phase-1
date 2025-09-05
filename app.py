import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from my DevOps Project!"

@app.route("/healthz")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # <-- Render will inject PORT
    app.run(host="0.0.0.0", port=port)
