from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def vegetables(request):
    template = loader.get_template('vegetables.html')
    return HttpResponse(template.render())