from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from .models import BoardModel
from django.contrib.auth.decorators import login_required

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
    return render(request, 'boardapp/signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'boardapp/login.html', {'context': 'ログインに失敗しました'})
    else:
        return render(request, 'boardapp/login.html', {})

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'boardapp/list.html', {'object_list': object_list})