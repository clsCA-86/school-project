import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Name",
            "class": "class",
            "starting_year": "year",
            "total_attendance": 23,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "time"
        },
    "852741":
        {
            "name": "Name",
            "class": "class",
            "starting_year": "year",
            "total_attendance": 23,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "time"
        },
    "963852":
        {
            "name": "Name",
            "class": "class",
            "starting_year": "year",
            "total_attendance": 23,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "time"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
