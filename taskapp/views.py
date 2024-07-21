from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import task
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        new_task = task(user=request.user,task_name=task_name)
        new_task.save()
    
    all_tasks = task.objects.filter(user = request.user)
    context = {
        'tasks': all_tasks
    }
    return render(request, 'taskapp/task.html',context)

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
        
        return redirect('login')
    return render(request,'taskapp/register.html',{})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request,validate_user)
            return  redirect('home-page')
        else:
            messages.error(request,'wrong username or password')
            return redirect('login')
    
    return render(request,'taskapp/login.html',{})

@login_required
def DeleteTask(request, id):
    get_task = get_object_or_404(task, id=id, user=request.user)
    get_task.delete()
    return redirect('home-page')

@login_required
def Update(request, id):
    get_task = get_object_or_404(task, id=id, user=request.user)
    get_task.status = True
    get_task.save()
    return redirect('home-page')
