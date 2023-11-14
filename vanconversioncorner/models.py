from vanconversioncorner import db

# code used from python standard library, see README credits
from datetime import datetime


class Question(db.Model):
    # schema for Question model
    id = db.Column(db.Integer, primary_key=True)
    question_title = db.Column(db.String(50), unique=True, nullable=False)
    question_body = db.Column(db.Text, nullable=False)
    # code used from python standard library, see README credits
    question_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship(
        "Comment", backref="category", cascade="all, delete", lazy=True)

    def __repre__(self):
        return "#{0} - Question: {1} | Further Information: {2}".format(
            self.id, self.question_title, self.question_body)


class Comment(db.Model):
    # schema for Comment model
    id = db.Column(db.Integer, primary_key=True)
    comment_body = db.Column(db.Text, nullable=False)
    # code used from python standard library, see README credits
    comment_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey(
        "question.id", ondelete="CASCADE"))

    def __repre__(self):
        return "#{0} - Comment: {1} | {2}".format(
            self.id, self.comment_body, self.comment_timestamp)
