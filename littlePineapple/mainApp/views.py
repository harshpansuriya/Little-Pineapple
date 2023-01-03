from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Skillers


def home(request):
    skillers_data = Skillers.objects.all()
    template = loader.get_template('index.html')
    context = {
        'skillers': skillers_data,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    return render(request, 'about.html')
