from django.shortcuts import render
from .models import *
# Create your views here.
def HomeView(request):
    return render(request,'todoapp/home.html')
