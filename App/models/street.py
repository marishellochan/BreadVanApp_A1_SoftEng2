from App.database import db
from App.models.user import User
from App.models.drive import Drive 

class Street(db.Model):
    street_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    street_name = db.Column(db.String(100), nullable=False)
    street_city = db.Column(db.String(100), nullable=False)

    residents = db.relationship('Resident', backref='street', lazy=True, cascade="all, delete-orphan")
    drives = db.relationship('Drive', backref='street', lazy=True, cascade="all, delete-orphan")
    

    def __init__(self, street_name, street_city):
        self.street_name = street_name
        self.street_city = street_city
    