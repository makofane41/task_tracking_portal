from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import aauthenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'taskapp/task.html',{})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 7:
            messages.error(request, 'Password is too short, required 7 char')
            return redirect('register')
        
        find_all_username = User.objects.filter(username=username)
        if find_all_username:
             messages.error(request, 'username alredy exisist')
             return redirect('register')

        new_user = User.objects.create_user(username = username,email=email, password=password )
        new_user.save()
        messages.success(request,'Successfully registered')
        #redirect user to login page
        return redirect('login')
    return render(request,'taskapp/register.html',{})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = aauthenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return  redirect('home-page')
        else:
            messages.error(request,'wrong username or password')
            return redirect('login')


    return render(request,'taskapp/login.html',{})