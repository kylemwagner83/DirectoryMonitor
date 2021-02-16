from enum import unique
import os
from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.sql.schema import Column



database_file = "sqlite:///Data/MediaDatabase.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
engine = create_engine("sqlite:///Data/MediaDatabase.db")
Session = sessionmaker(bind=engine)




class Games(db.Model):
    name = Column(db.String, unique=True, primary_key=True)
    downloaded_on =Column(db.String)
    played = Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Game: {self.name}>"
        




@app.route("/")
@app.route("/index")
def index():
    games = None
    games = Games.query.all()
    return render_template("index.html", games = games)


if __name__ == "__main__":
    app.run(port=5100)
    #app.run(host="0.0.0.0", port=6000, debug=False)
