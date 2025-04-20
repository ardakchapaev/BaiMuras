from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from BaiMuras"
