from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import register
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def login(request):
    if request.method == 'POST':
        ul = request.POST['username']
        pl = request.POST['password']
        user = auth.aunthicate(username=ul, password=pl)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'please enter correct username or password')
    else:
        return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        es = request.POST['email']
        ps = request.POST['password']
        us = request.POST['username']
        obj_reg = register(email=es, password=ps, username=us)

        obj_reg.save()
        # print(obj_reg)
    return render(request, 'login.html')


def views(request):
    return render(request, 'viewsbutton.html')
