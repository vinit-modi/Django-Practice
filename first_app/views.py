from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(Request):
    my_dict = {'insert_me':"Hello, i am from vies.py"}
    return render(Request, 'first_app/index.html', context=my_dict)

def home(Request):
    return HttpResponse("Home page")