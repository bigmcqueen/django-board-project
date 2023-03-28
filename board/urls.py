from django.urls import path, include

from .views import *

urlpatterns = [
    path('', top, name='top'),
    path('signup/', signup, name='signup')
]