from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1,'name':'Lets learn python!'},
    {'id':2,'name':'Design with me!'},
    {'id':3,'name':'Frontend developers'},
    {'id':4,'name':'AI Engine!!!'},
]

def home(request):
    context = {"Data":rooms}
    return render(request,'home.html',context)

def room(request):
    return render(request,'room.html')
