
# entities\request.py
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
import flask_login
import json

db = SQLAlchemy()
ma = Marshmallow()

class Request(db.Model):
    # Name of the table in our database
    __tablename__ = 'Requests' 
    # Defining the columns
    requestid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    status = db.Column(db.String(25), unique=False, nullable=True)
    createdby = db.Column(db.String(25), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now().isoformat())
    updated_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now().isoformat())
    updated = db.Column(db.Boolean, default=False)
    def get_id(self):
        return text_type(self.requestid)

class RequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'status')