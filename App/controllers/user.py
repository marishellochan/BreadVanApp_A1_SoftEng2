from App.models import User
from App.database import db
from App.models.user import Resident

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    result = db.session.execute(db.select(User).filter_by(username=username))
    return result.scalar_one_or_none()

def get_user(id):
    return db.session.get(User, id)

def get_all_users():
    return db.session.scalars(db.select(User)).all()

def get_all_users_json():
    users = get_all_users()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        # user is already in the session; no need to re-add
        db.session.commit()
        return True
    return None

def create_resident(username, password, street_id):
    newresident = Resident(username=username, password=password, street_id=street_id)
    db.session.add(newresident)
    db.session.commit()
    return newresident

def get_resident(resident_id):
    resident = db.session.execute(db.select(Resident).filter_by(resident_id=resident_id)).scalar_one_or_none()
    return resident 

def get_residents_from_street(street_id):
    residents = db.session.execute(db.select(Resident).filter_by(street_id=street_id)).scalars().all()
    return residents
