import click, pytest, sys
from flask.cli import with_appcontext, AppGroup
from datetime import datetime
from App.database import db, get_migrate
from App.models import User, Drive
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, get_all_residents_from_Street, driver_schedules_drive, get_driver, get_resident, get_Street)
from App.controllers import (get_drive, get_resident_by_username_password, get_driver_by_license_password)
from App.controllers.requests import create_request, get_requests


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli



'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

@test.command("street", help="Run Residents from Street tests")
@click.argument("street_id", default="all")
def residents_from_street_tests_command(street_id):
    if street_id == "1": 
        print(get_all_residents_from_Street(1))
    else: 
        print('No street with that ID')

@test.command("schedule_drive", help="Run schedule drive tests")
def schedule_drive_tests_command():
    license_number = input("Enter driver license number: ")
    password = input('Enter your password: ')
    driver = get_driver_by_license_password(license_number,password)
    if driver:
    #     date = date(input("Enter drive date (YYYY-MM-DD): "))
        try:
            date_input = input("Enter drive date (YYYY-MM-DD): ")
            drive_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        try:
            street_id = int(input("Enter street ID: "))
        except ValueError:
            print("Invalid street ID. Please enter a number.")
            return
        drive = driver_schedules_drive(driver, drive_date, street_id)
        print(drive.get_json())
        print('Drive scheduled')
        print('Scheduled drives for driver:')
        for drive in driver.drives:
            print(drive.get_json())
    else:
        print('No driver with that ID')

@test.command("view_inbox", help="Run view inbox tests")
def view_inbox_tests_command():
    username = input("Enter resident username: ")
    password = input("Enter resident password: ")
    resident = get_resident_by_username_password(username, password)
    if resident:
        street = get_Street(resident.street_id)
        if street: 
            drives = street.drives 
            if drives: 
                for drive in drives:
                    print(drive.get_json())
            else:
                print('No drives scheduled on your street')
        else:
            print('No street with that ID')
            return    
    else:
        print('No resident with that ID')

@test.command("request", help="Run request tests") # need to add where the drive is from the resident's street
def send_request_tests_command():
    username = input("Enter resident username: ")
    password = input("Enter resident password: ")
    resident = get_resident_by_username_password(username, password)
    if resident: 
        try: 
            drive_id = int(input("Enter drive ID to request stop at your street: "))
            drive = get_drive(drive_id)
        except ValueError:
            print("Invalid drive ID. Please enter a number.")
            return
        if drive: 
            print(drive.get_json())
            request = create_request(resident, drive.drive_id)
            print(request.get_json())
            print('Request sent')
        else:
            print('No drive with that ID')
            return
    else:
        print('No resident with that ID')
        return 

@test.command("view_driver_status", help="Run view driver status tests") 
def view_driver_status_tests_command():
        username = input("Enter resident username: ")
        password = input("Enter resident password: ")
        resident = get_resident_by_username_password(username, password)
        if resident: 
            # print(resident.get_json())

            drive_ID= input("Enter drive ID to view driver status: ")
            drive = get_drive(drive_ID)
            if drive:
                driver_license = drive.license_number
                driver = get_driver(driver_license)
                if driver:
                    print('Driver status:')
                    print(driver.get_json_status())
                else:
                    print('No driver with that ID')
                    return
            else: 
                print('No drive with that ID')
                return
        else: 
            print('No resident with that username or password')
            return
        
@test.command("view_drive_requests", help="Run all tests")
def view_drive_stops():
    drive_id = input('Enter drive ID to see stops: ')
    drive = get_drive(drive_id)
    if drive: 
        get_requests(drive)
    else: 
        print('Drive does not exist')
        return


app.cli.add_command(test)