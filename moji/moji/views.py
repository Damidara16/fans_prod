from django.views import View
from django.shortcuts import render, redirect, Http404

def home(request):
    return render(request, 'home/home.html')
