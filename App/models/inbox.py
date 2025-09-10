from App.database import db

class Inbox(db.Model):
    inbox_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    resident_id = db.Column(db.Integer, db.ForeignKey('resident.id'), nullable=False)

    drives = db.relationship('Drive', secondary='driveinbox', backref=db.backref('residentinboxes', lazy=True))

    def __init__(self, resident_id):
        super().__init__()
        self.resident_id = resident_id

    def get_json(self):
        return{
            'inbox_id': self.inbox_id,
            'resident_id': self.resident_id
        }
