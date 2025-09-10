from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
class Driver(User):
    liscense_number = db.Column(db.String(20), nullable=False, unique=True)
    
    drives = db.relationship('Drive', backref='driver', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, liscense_number):
        super().__init__(username, password)
        self.liscense_number = liscense_number

    def get_json(self):
        user_json = super().get_json()
        user_json += { 'liscense_number' : self.liscense_number}
        return user_json
    

class Resident(User):
    resident_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    street_id = db.Column(db.Integer, db.ForeignKey('street.street_id'), nullable=False) 

    requests = db.relationship('Request', backref='resident', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, street_id):
        super().__init__(username, password)
        self.street_id = street_id  

