from __init__ import db


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
