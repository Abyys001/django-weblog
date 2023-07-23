from django.shortcuts import render
from django.http import HttpResponse

# importing models
from .models import Profile


# Create your views here.

def page(request):
    return HttpResponse("hello world")