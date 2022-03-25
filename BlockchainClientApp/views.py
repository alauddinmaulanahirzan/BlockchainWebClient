from django.shortcuts import render
# Firebase Section
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
from google.cloud import storage

# Create your views here.
# Firebase Auth
databaseURL = "https://iot-db-b4768-default-rtdb.asia-southeast1.firebasedatabase.app/"
cred = credentials.Certificate("iot-db-adminsdk.json")
app = firebase_admin.initialize_app(cred,{'databaseURL':databaseURL})
reference = db.reference("/")

def index(request):
    total_machines = 0
    total_dsessions = 0
    total_tsessions = 0
    total_blocks = 0
    query = reference.get()
    # Get Data Summary
    for machine in query.keys():    # By Machine
        total_machines += 1
        dsessions = reference.child(machine).get()
        for dsession in dsessions.keys():     # By Date
            total_dsessions += 1
            tsessions = reference.child(machine).child(dsession).get()
            for tsession in tsessions.keys():  # By Time
                total_tsessions += 1
                blocks = reference.child(machine).child(dsession).child(tsession).get()
                for block in blocks.keys():
                    total_blocks += 1

    context = {
        'total_machines':total_machines,
        'total_dsessions':total_dsessions,
        'total_tsessions':total_tsessions,
        'total_blocks':total_blocks
        }
    return render(request, 'Home.html', context)

def getStatus(request):
    name = reference.get().keys()
    print(name)

    context = {
        'name':name
        }
    return render(request, 'Blockchain-Status.html', context)

def getAbout(request):
    context = {'name':"A"}
    return render(request, 'About.html', context)
