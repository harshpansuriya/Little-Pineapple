from django.shortcuts import render, redirect
from django.http import HttpResponse
from SkillersApp.models import User
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages

def index(request):
    requestedUser = User.objects.all()
    return render(request, "index.html", {"user": requestedUser})

def about(request):
    requestedUser = User.objects.all()
    return render(request, "about.html", {"user": requestedUser})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request=request, template_name="register.html", context={"register_form": form})