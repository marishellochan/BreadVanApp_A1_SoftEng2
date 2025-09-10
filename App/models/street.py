from App.database import db

class Street(db.Model):
    street_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    street_name = db.Column(db.String(100), nullable=False)
    street_city = db.Column(db.String(100), nullable=False)

    residents = db.relationship('Resident', backref='street', lazy=True, cascade="all, delete-orphan")
    drives = db.relationship('Drive', backref='street', lazy=True, cascade="all, delete-orphan")
    

    def __init__(self, street_name, street_city):
        self.street_name = street_name
        self.street_city = street_city

    def get_json(self):
        return{
            'street_id': self.street_id,
            'street_name': self.street_name,
            'street_city': self.street_city
        }
    