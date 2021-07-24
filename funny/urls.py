from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'funny'
urlpatterns = [         
    path('dashboard',view=views.funnydashboard, name='funnydashboard'),       

      
]