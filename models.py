from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ScrapedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)
    word_frequency = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

