from App.controllers import drive
from App.database import db
from App.models.requests import Request
from App.models.user import Resident

def create_request(resident, drive_id):
    newrequest = Request(drive_id=drive_id, resident_id=resident.user_id)
    resident.requests.append(newrequest)
    db.session.commit()
    return newrequest

def get_requests(drive):
    for request in drive.requests:
        print(request.get_json())

