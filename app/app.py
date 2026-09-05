from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Version 3 — Déployé automatiquement malgré la panne du leader !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
