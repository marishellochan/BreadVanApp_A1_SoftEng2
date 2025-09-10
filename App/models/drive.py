from App.database import db

class Drive(db.Model):
    drive_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.driver_id'), nullable=False)
    street_id = db.Column(db.Integer, db.ForeignKey('street.street_id'), nullable=False)

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
    