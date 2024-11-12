from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def index(request):
    return render(request, "login/index.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, "Account created successfully!")
            return redirect('home')  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})