"""Define URL patterns for users"""

import django
from django.urls import path, include
from . import views

app_name = 'users'  #<<-- This helps Django to distinguish URLs from URLs belonging to other apps
urlpatterns = [
    #include default atuh urls
    path('',include('django.contrib.auth.urls')), #<<-- accessing URLs provided by Django in user name space

    #Registration Page
    path('register/',views.register, name='register')
]
