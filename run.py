import os
from vanconversioncorner import app
from flask import Flask

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")


with app.app_context():
    db.create_all()
