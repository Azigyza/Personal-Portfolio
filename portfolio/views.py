from django.shortcuts import render
from django.http import HttpResponse
from .models import Project # this statement import the models into our view area

def home(request):
    projects = Project.objects.all()   # this grabs all the objects from our the DB into the home page
    return  render(request,  'portfolio/home.html',  {'projects': projects}) # this is the variable from above
