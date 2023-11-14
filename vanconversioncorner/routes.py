from flask import render_template
from vanconversioncorner import app, db
from vanconversioncorner.models import Question, Comment


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/post-your-questions")
def postYourQuestions():
    return render_template("post-your-questions.html")


@app.route("/media")
def media():
    return render_template("media.html")
