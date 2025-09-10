from App.database import db
from App.models.user import User
from App.models.drive import Drive
from App.models.driveinbox import DriveInbox


class Inbox(db.Model):
    inbox_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    

    def __init__(self):
        pass

    def get_json(self):
        return{
            'inbox_id': self.inbox_id
        }


class ResidentInbox(Inbox):
    resident_id = db.Column(db.Integer, db.ForeignKey('resident.id'), nullable=False)

    drives = db.relationship('Drive', secondary='driveinbox', backref=db.backref('residentinboxes', lazy=True))

    def __init__(self, resident_id):
        super().__init__()
        self.resident_id = resident_id
