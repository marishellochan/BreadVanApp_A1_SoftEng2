from .user import create_user, create_resident, get_all_residents
from .street import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    db.session.add(create_street("Baker Street", "London"))
    db.session.add(create_street("Fleet Street", "London"))
    db.session.add(create_street("High Street", "Oxford"))
    db.session.add(create_resident("shelly", "password", 1))
    db.session.add(create_resident("john", "password", 1))
    db.session.commit()


    for street in get_all_streets():
        print(street.get_json())

    for resident in get_all_residents():
        print(resident.get_json())


