from vanconversioncorner import db


class Question(db.Model):
    # schema for Question model
    id = db.Column(db.Integer, primary_key=True)

    def__repre__(self):
        return self


class Comment(db.Model):
    # schema for Comment model
    id = db.Column(db.Integer, primary_key=True)

    def__repre__(self):
        return self
