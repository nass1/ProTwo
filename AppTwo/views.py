from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

def index(request):
    return HttpResponse("<em>My Second App</em>")


def help(request):
    my_dict = {"abc": "and here come the bom from abc or views.py"}

    return render(request, "index.html", context=my_dict)


def users(request):
    my_dict = {"users": User.objects.all()}

    return render(request, "user.html", context=my_dict)
