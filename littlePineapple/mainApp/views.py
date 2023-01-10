from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from rest_framework import viewsets
from .serializers import TodoSerializer

from .models import Skillers



class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Skillers.objects.all()


def home(request):
    skillers_data = Skillers.objects.all()
    template = loader.get_template('index.html')
    context = {
        'skillers': skillers_data,
    }
    return HttpResponse(template.render(context, request))


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already Exists.")
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is already Exists.")
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password,)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password not the same!")
            return redirect('register')

    else:
        return render(request, 'registration/register.html')


@login_required
def addSkill(request):



    return render(request, 'addskill.html')


def about(request):
    return render(request, 'about.html')
