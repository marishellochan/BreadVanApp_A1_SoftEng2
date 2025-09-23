from App.database import db
from App.models.drive import Drive

class Request(db.Model):
    request_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.drive_id'), nullable=False)
    resident_id = db.Column(db.Integer, db.ForeignKey('resident.user_id'), nullable=False)


    def __init__(self, drive_id,resident_id):
        self.drive_id = drive_id
        self.resident_id = resident_id

    def get_json(self):
        drive = Drive.query.get(self.drive_id)
        return {
            'request_id': self.request_id,
            'drive_id': self.drive_id,
            'resident_id': self.resident_id,
            'license_number': drive.license_number,
            'date': drive.date.strftime('%Y-%m-%d'), 
            'street_id': drive.street_id 
        }