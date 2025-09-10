from App.database import db
from App.models.street import Street
from App.models.user import Driver
from App.models.drive import Drive

def schedule_drive(driver_id, date, street_id):
    newdrive = Drive(driver_id=driver_id, date=date, street_id=street_id)
    db.session.add(newdrive)
    db.session.commit()
    return newdrive

def get_drive(drive_id):
    return db.session.get(Drive, drive_id)

def get_all_drives_of_driver(driver_id):
    drives = db.session.execute(db.select(Drive).filter_by(driver_id=driver_id)).scalars().all()
    return drives
