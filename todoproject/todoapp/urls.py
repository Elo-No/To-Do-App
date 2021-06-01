from django.urls import path
from .views import *

app_name='todoapp'
urlpatterns = [
    path('',HomeView,name="home_url"),
]

