from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Привет, это Mini App для Telegram!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
