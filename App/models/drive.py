from App.database import db
from App.models.street import Street
from App.models.inbox import Inbox
from App.models.driveinbox import DriveInbox

class Drive(db.model):
    drive_id = db.column(db.Integer, unique=True, nullable=False, primary_key=True)
    date = db.column(db.DateTime, nullable=False)
    driver_id = db.column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    street_id = db.column(db.Integer, db.ForeignKey('street.street_id'), nullable=False)

    #residentinboxes = db.relationship('ResidentInbox', secondary='driveinbox', backref=db.backref('drives', lazy=True))
    

    def __init__(self, driver_id, date, street_id):
        self.driver_id = driver_id
        self.date = date
        self.street_id = street_id

    def get_json(self):
        return{
            'drive_id': self.drive_id,
            'driver_id': self.driver_id,
            'date': self.date,
            'street_id': self.street_id 
        }
    