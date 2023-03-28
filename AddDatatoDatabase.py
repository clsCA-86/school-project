import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-4f391-default-rtdb.firebaseio.com/"
})

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
