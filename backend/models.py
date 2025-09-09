from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db=SQLAlchemy()


    
class Tasks(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),nullable=False)
    completed=db.Column(db.Boolean,default=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)