from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

@login_required
def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'boardapp/detail.html', {'object': object})

@login_required
def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')

@login_required
def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read += 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('list')