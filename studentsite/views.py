from django.shortcuts import render
from django.http import HttpResponse
from .models import studentdetails
from django.shortcuts import render
# Create your views here.


def studentform(request):
    if request.method == 'POST':
        roll = request.POST['roll']
        name = request.POST['name']
        regno = request.POST['regno']
        semister = request.POST['semister']
        courses = request.POST['courses']
        obj_stu = studentdetails(
            roll=roll, name=name, regno=regno, semister=semister, courses=courses)
        obj_stu.save()
    return render(request, 'file.html')


def showresult(request):
    obj_result = studentdetails.objects.all()
    return render(request, 'views.html', {'obj1': obj_result})
