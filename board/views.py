from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

from .forms import *

# Create your views here.
def top(request):
    template_name = 'board/top.html'
    return render(request, template_name)

def signup(request):
    template_name = 'board/signup.html'
    form = SignUpForm(request.POST or None)
    params = {'form': form}
    # フォームの送信時にエラーが無いかをチェックする
    if form.is_valid():
        # cleaned_data[フィールド名]で値をそれぞれ変数へ入れていく
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            # User.objects.create_user()を実行した時点で、userは作成される
            user = User.objects.create_user(name, email, password)
        except IntegrityError:
            params['context'] = 'このユーザーはすでに登録されています'
            return render(request, template_name, params)

    return render(request, template_name, params)