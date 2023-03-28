from django.shortcuts import render

# Create your views here.
def top(request):
    return render(request, 'board/top.html')

def signup(request):
    return render(request, 'board/signup.html', {})