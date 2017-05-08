from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . forms import UserForm

def index(request):
    return HttpResponse("<em>My Second App</em>")


def help(request):
    my_dict = {"abc": "and here come the bom from abc or views.py"}

    return render(request, "index.html", context=my_dict)


def users(request):
    my_dict = {"users": User.objects.all()}

    return render(request, "user.html", context=my_dict)

def contact(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ("error forms invalid")


    my_dict = {"users": UserForm}

    return render(request, "forms.html", context=my_dict)
