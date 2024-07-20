from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'taskapp/task.html',{})

def register(request):
    return render(request,'taskapp/register.html',{})

def login(request):
    return render(request,'taskapp/login.html',{})