from vanconversioncorner import db
# code used from python standard library, see README credits
from datetime import datetime


class Question(db.Model):
    # schema for Question model
    id = db.Column(db.Integer, primary_key=True)
    question_title = db.Column(db.String(50), unique=True, nullable=False)
    question_body = db.Column(db.Text, nullable=False)
    question_timestamp = db.Column(db.DateTime, default=datetime.utcnow) # code used from python standard library, see README credits
    comments = db.relationship(
        "Comment", backref="category", cascade="all, delete", lazy=True)

    def __repre__(self):
        return self.question_title, self.question_body


class Comment(db.Model):
    # schema for Comment model
    id = db.Column(db.Integer, primary_key=True)
    comment_body = db.Column(db.Text, nullable=False)
    comment_timestamp = db.Column(db.DateTime, default=datetime.utcnow) # code used from python standard library, see README credits
    question_id = db.Column(db.Integer, db.ForeignKey(
        "question.id", ondelete="CASCADE"))

    def __repre__(self):
        return self.comment_body
