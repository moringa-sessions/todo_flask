from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email=db.Column(db.String(128), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    password=db.Column(db.String(128), nullable=False)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description=db.Column(db.String(256), nullable=False)
    is_complete = db.Column(db.Boolean, default=False )
    deadline = db.Column(db.String(20), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False )
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), nullable=False )

