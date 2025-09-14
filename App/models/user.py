from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models.drive import Drive
from App.models.street import Street
from App.models.requests import Request

class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.user_id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
class Driver(User):
    __mapper_args__ = {'polymorphic_identity': 'driver'}
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True, nullable=False, primary_key=True)
    license_number = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)
    
    drives = db.relationship('Drive', backref='driver', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, license_number):
        super().__init__(username, password)
        self.license_number = license_number

    def get_json(self):
        user_json = super().get_json()
        user_json.update({ 'license_number' : self.license_number})
        return user_json
    

class Resident(User):
    __mapper_args__ = {'polymorphic_identity': 'resident'}
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True, nullable=False, primary_key=True)
   # resident_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    street_id = db.Column(db.Integer, db.ForeignKey('street.street_id'), nullable=False) 

    requests = db.relationship('Request', backref='resident', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, street_id):
        super().__init__(username, password)
        self.street_id = street_id  

    def get_json(self):
        user_json = super().get_json()
        user_json.update({ 'street_id' : self.street_id })
        return user_json



