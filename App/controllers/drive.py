from App.database import db
from App.models.street import Street
from App.models.user import Driver
from App.models.drive import Drive

def schedule_drive(license_number, date, street_id):
    newdrive = Drive(license_number=license_number, date=date, street_id=street_id)
    db.session.add(newdrive)
    db.session.commit()
    return newdrive

def get_drive(drive_id):
    return Drive.query.get(drive_id)

def get_all_drives_of_driver(driver_id):
    drives = Drive.query.filter_by(license_number=license_number).all()
    return drives

