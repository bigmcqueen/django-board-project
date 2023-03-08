from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'boardapp/signup.html', {'name': 'Tom'})
        except IntegrityError:
            return render(request, 'boardapp/signup.html', {'error': 'このユーザーはすでに登録されています！'})
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'boardapp/login.html', {'context': 'logged in'})
        else:
            return render(request, 'boardapp/login.html', {'context': 'not logged in'})
    return render(request, 'boardapp/login.html', {'context': 'get method'})