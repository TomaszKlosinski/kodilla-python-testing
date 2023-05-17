from . import db
import datetime

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"<Entry {self.id} {self.title} {self.body[:50]} ...>"