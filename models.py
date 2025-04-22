from datetime import datetime
from database import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), default="running")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
