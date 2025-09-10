from App.database import db
from App.models.street import Street

def create_street(street_name, street_city):
    newstreet = Street(street_name=street_name, street_city=street_city)
    db.session.add(newstreet)
    db.session.commit()
    return newstreet

def get_all_streets():
    return db.session.scalars(db.select(Street)).all()

def get_Street(street_id):
    return db.session.get(Street, street_id)

def get_all_residents_from_Street(street_id):
    street = get_Street(street_id)
    if street:
        return street.residents
    else:
        return None