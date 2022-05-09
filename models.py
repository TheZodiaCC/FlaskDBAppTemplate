from __init_ import db


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
