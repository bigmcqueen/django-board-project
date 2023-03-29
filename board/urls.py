from django.urls import path, include

from .views import *

urlpatterns = [
    path('', top, name='top'),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='login'),
    path('list/', list_view, name='list'),
]