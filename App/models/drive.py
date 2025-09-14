from App.database import db
from datetime import datetime

class Drive(db.Model):
    drive_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    license_number = db.Column(db.String(20), db.ForeignKey('driver.license_number'), nullable=False)
    street_id = db.Column(db.Integer, db.ForeignKey('street.street_id'), nullable=False)

    #residentinboxes = db.relationship('ResidentInbox', secondary='driveinbox', backref=db.backref('drives', lazy=True))
    

    def __init__(self, license_number, date, street_id):
        self.license_number = license_number
        self.date = date
        self.street_id = street_id

    def get_json(self):
        return{
            'drive_id': self.drive_id,
            'license_number': self.license_number,
            'date': self.date.strftime('%Y-%m-%d'), 
            'street_id': self.street_id 
        }
    