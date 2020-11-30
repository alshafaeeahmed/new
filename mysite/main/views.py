from django.shortcuts import render
from django.http import HttpResponse
from .models import Volunteer, Elderly


# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome to our site!<h1>")


# Create your views here.


def index(response, id):
    ls = Volunteer.objects.get(id=id)
    return (response,"main/list.html",{"ls":ls})


def home(response):
    return (response,"main/home.html/",{"name":"test"})
