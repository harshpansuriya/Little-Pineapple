from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Skillers


def home(request):
    skillers_data = Skillers.objects.all()
    template = loader.get_template('index.html')
    context = {
        'skillers': skillers_data,
    }
    return HttpResponse(template.render(context, request))


@login_required
def addSkill(request):

    return render(request, 'addskill.html')


def about(request):
    return render(request, 'about.html')
