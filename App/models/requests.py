from App.database import db

class Request(db.Model):
    request_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.drive_id'), nullable=False)
    resident_id = db.Column(db.Integer, db.ForeignKey('resident.resident_id'), nullable=False)


    def __init__(self, drive_id):
        self.drive_id = drive_id

    def get_json(self):
        return {
            'request_id': self.request_id,
            'drive_id': self.drive_id,
        }