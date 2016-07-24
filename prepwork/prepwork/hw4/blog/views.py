# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Employee

def index(resquest):
    emps = Employee.objects.all()
    return render_to_response('index.html',{'emps':emps})


