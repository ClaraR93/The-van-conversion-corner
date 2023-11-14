from flask import render_template
from vanconversioncorner import app, db
from vanconversioncorner.models import Question, Comment


@app.route("/")
def home():
    return render_template("base.html")
