from django.shortcuts import render, redirect

from .models import Board
from .forms import BoardForm

# Create your views here.


def board(request):
    template_name = 'board/board.html'
    contents = Board.objects.all()
    form = BoardForm(request.POST or None)
    params = {'contents': contents, 'form': form}
    if form.is_valid():
        board = form.save(commit=False)
        board.save()
        return redirect('board:board')
    return render(request, template_name, params)
