from django.urls import path

from .views import board

app_name = 'board'

urlpatterns = [
    path('', board, name='board'),
]
