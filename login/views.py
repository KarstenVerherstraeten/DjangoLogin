from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomRegistrationForm, TaskForm
from .models import Task

def index(request):
    return render(request, "login/index.html")

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, "Account created successfully!")
            return redirect('login:dashboard')  # Redirect after registration
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def dashboard(request):
    return render(request, 'pages/dashboard.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('login:dashboard')
    else:
        form = TaskForm()
    return render(request, 'pages/addTask.html', {'form': form})

def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'pages/viewTasks.html', {'tasks': tasks})