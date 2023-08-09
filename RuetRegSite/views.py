# ai module ta amak function er moddhe kono kisu return korte hole help korbe
from django.http import HttpResponse
import datetime
# ai render module ta amak html template ta ke use korte help korbe
from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    return render(request, 'homebutton.html')
