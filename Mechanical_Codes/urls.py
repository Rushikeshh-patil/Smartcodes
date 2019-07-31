#This is where mapping happens. Say we have 10 different pages with 10 different view functions written in the views.py file, then we will have 10
# maps here. Hence We will need to import our views (Functions) here
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mechanical, name='Mechanical'),
    path('about/', views.about, name='About'),

]