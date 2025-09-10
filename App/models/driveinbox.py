from App.database import db
from App.models.user import User
from App.models.drive import Drive
from App.models.inbox import Inbox 

class DriveInbox(db.model):
    __tablename__ = 'driveinbox'
    driveinbox_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.drive_id'), nullable=False)
    inbox_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)

    def __init__(self, drive_id, inbox_id):
        self.drive_id = drive_id
        self.inbox_id = inbox_id

