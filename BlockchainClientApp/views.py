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
    #accessing our firebase data and storing it in a variable
    data = reference.get()
    total_device = len(data)

    context = {
        'total_device':total_device
        }
    return render(request, 'Home.html', context)

def getData(request):
    #accessing our firebase data and storing it in a variable
    name = reference.get().keys()
    print(name)

    context = {
        'name':name
        }
    return render(request, 'tabledata.php', context)
