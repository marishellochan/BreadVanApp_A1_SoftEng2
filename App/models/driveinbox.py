from App.database import db

class DriveInbox(db.Model):
    __tablename__ = 'driveinbox'
    driveinbox_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.drive_id'), nullable=False)
    inbox_id = db.Column(db.Integer, db.ForeignKey('inbox.inbox_id'), nullable=False)

    def __init__(self, drive_id, inbox_id):
        self.drive_id = drive_id
        self.inbox_id = inbox_id

