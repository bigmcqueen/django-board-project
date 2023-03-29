from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

from .forms import *

# Create your views here.
def top(request):
    template_name = 'board/top.html'
    return render(request, template_name)

def signup(request):
    template_name = 'board/signup.html'
    form = SignInAndSignUpForm(request.POST or None)
    params = {'form': form}
    # フォームの送信時にエラーが無いかをチェックする
    if form.is_valid():
        # cleaned_data[フィールド名]で値をそれぞれ変数へ入れていく
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            # User.objects.create_user()を実行した時点で、userは作成される
            user = User.objects.create_user(username=email, password=password)
        except IntegrityError:
            params['context'] = 'このユーザーはすでに登録されてるお (＾ω＾≡＾ω＾)'
            return render(request, template_name, params)
        
    return render(request, template_name, params)

def signin(request):
    template_name = 'board/signin.html'
    form = SignInAndSignUpForm(request.POST or None)
    params = {'form': form}
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success pag
            redirect('top')
        else:
            # Return an 'invalid login' error message.
            params['context'] = '違うお (＾ω＾≡＾ω＾)'
            return render(request, template_name, params)
        
    return render(request, template_name, params)

def list_view(request):
    template_name = 'board/list.html'
    return render(request, template_name, {})
