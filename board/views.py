from django.shortcuts import render
from .forms import *

# Create your views here.
def top(request):
    return render(request, 'board/top.html')

def signup(request):
    if request.method == 'POST':
        print('POST')
        return render(request, 'board/signup.html', {'form': BoardForm})
    else:
        print('NOT POST')
        return render(request, 'board/signup.html', {'form': BoardForm})
    return render(request, 'board/signup.html', {'form': BoardForm})