from .user import create_user, create_resident, get_all_residents, create_driver, get_all_drivers, schedule_drive
from .street import *
from .drive import *
from App.database import db
from datetime import date



def initialize():
    db.drop_all()
    db.create_all()
    db.session.add(create_street("Baker Street", "London"))
    db.session.add(create_street("Fleet Street", "London"))
    db.session.add(create_street("King Street", "Manchester"))
    db.session.add(create_street("High Street", "Oxford"))
    db.session.add(create_driver("sherlock", "password", "264721", "available", "Oxford"))
    db.session.add(create_driver("watson", "password", "235612", "available", "London" ))
    db.session.add(create_driver("holmes", "password", "987654", None, None))
    db.session.add(create_driver("gregson", "password", "123456", "available", "Manchester" ))
    db.session.add(create_resident("shelly", "password", 1))
    db.session.add(create_resident("john", "password", 1))
    db.session.add(schedule_drive("264721", date.fromisoformat('2024-12-01'), 1))
    db.session.add(schedule_drive("235612", date.fromisoformat('2024-11-15'), 2))
    db.session.commit()


    for street in get_all_streets():
        print(street.get_json())

    for resident in get_all_residents():
        print(resident.get_json())

    for driver in get_all_drivers():
        print(driver.get_json())

    for drive in get_all_drives():
        print(drive.get_json())


