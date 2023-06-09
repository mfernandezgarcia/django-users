from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
# Create your views here.

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "users": myusers
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
    myuser = User.objects.get(id=id)
    template = loader.get_template("detail.html")
    context = {
        "user": myuser
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())