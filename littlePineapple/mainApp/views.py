from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to the Little PineApple</h1><br/><p>Harsh's App</p>")
