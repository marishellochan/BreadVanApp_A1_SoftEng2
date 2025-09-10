from App.database import db
from App.models.user import User

class Request(db.Model):
    request_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.drive_id'), nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('resident.username'), nullable=False)


    def __init__(self, drive_id):
        self.drive_id = drive_id

    def get_json(self):
        return {
            'request_id': self.request_id,
            'drive_id': self.drive_id,
        }