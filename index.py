from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
name = "Ciaran"


@app.route("/")
def hello_world():
    return render_template("index.html", name=escape(name))
