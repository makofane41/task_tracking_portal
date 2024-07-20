from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import task
# Create your views here.

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
        #redirect user to login page
        return redirect('login')
    return render(request,'taskapp/register.html',{})

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

def DeleteTask(request, name):
    get_task = task.objects.get(user = request.user, task_name = name)
    get_task.delete()
    return redirect('home-page')

def Update(request, name):
     get_task = task.objects.get(user = request.user, task_name = name)
     get_task.status = True
     get_task.save()
     return redirect('home-page')

# def Update(request, name):
#     tasks = task.objects.filter(user=request.user, task_name=name)
#     if tasks.exists():
#         if tasks.count() == 1:
#             get_task = tasks.first()
#             get_task.status = True
#             get_task.save()
#             messages.success(request, 'Task updated successfully.')
#         else:
#             # Handle the case where multiple tasks are found
#             messages.warning(request, 'Multiple tasks found. Updating the first one.')
#             get_task = tasks.first()
#             get_task.status = True
#             get_task.save()
#     else:
#         # Handle the case where no tasks are found
#         messages.error(request, 'No task found with the given name.')

#     return redirect('home-page')