from App.database import db
from App.models.street import Street
from App.models.user import Resident

def create_street(street_name, street_city):
    newstreet = Street(street_name=street_name, street_city=street_city)
    db.session.add(newstreet)
    db.session.commit()
    return newstreet

def get_all_streets():
    return Street.query.all()

def get_Street(street_id):
    return Street.query.get(street_id)

def get_all_residents_from_Street(street_id):
    street = get_Street(street_id)
    if street: 
        return [resident.get_json() for resident in street.residents]
    return []
