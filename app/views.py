from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

url = "mongodb://localhost:27017"

client = MongoClient(url, server_api=ServerApi('1'))

db = client.benitton
db_user = db.user

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        user = {
            'username': username,
            'email': email,
            'firstname': 'firstname',
            'lastname': 'lastname',
            'role': role,
            'password': password,
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now()
        }
        db_user.insert_one(user)
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if db_user.find_one(username=username,password=password) is not None:return HttpResponse("User Found")
    return render(request,'signin.html')
