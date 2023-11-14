from vanconversioncorner import db


class Question(db.Model):
    # schema for Question model
    id = db.Column(db.Integer, primary_key=True)
    question_title = db.Column(db.String(50), unique=True, nullable=False)
    question_body = db.Column(db.Text, nullable=False)

    def__repre__(self):
        return self


class Comment(db.Model):
    # schema for Comment model
    id = db.Column(db.Integer, primary_key=True)
    comment_body = db.Column(db.Text, nullable=False)

    def__repre__(self):
        return self
