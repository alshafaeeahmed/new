from django.shortcuts import render
from django.http import HttpResponse
from .models import Volunteer, Elderly
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Create your views here.
def register(response):
    form = UserCreationForm()
    return render(response, "main/Volunteer.html")

def index(response):
    return render(response,"main/home.html")

