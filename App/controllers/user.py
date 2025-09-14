from App.models import User
from App.database import db
from App.models.user import Resident,Driver
from App.controllers.drive import schedule_drive

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

def get_resident(user_id):
    resident = Resident.query.get(user_id)
    return resident 

def get_all_residents():
    return Resident.query.all()

def get_residents_from_street(street_id):
    residents = Resident.query.filter_by(street_id=street_id).all()
    for resident in residents:
        print(resident.get_json())
    return 

def get_driver(license_number):
    driver = Driver.query.filter_by(license_number=license_number).first()
    return driver

def get_all_drivers():
    return Driver.query.all()

def create_driver(username, password, license_number):
    newdriver = Driver(username=username, password=password, license_number=license_number)
    db.session.add(newdriver)
    db.session.commit()
    return newdriver

def driver_schedules_drive(driver, date, street_id):
    drive = schedule_drive(driver.license_number, date, street_id)
    driver.drives.append(drive)
    db.session.commit()
    return drive