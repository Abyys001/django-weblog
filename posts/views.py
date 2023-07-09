from django.http import HttpResponse
from django.shortcuts import render

# my models
from .models import *


# Create your views here.
def post_list(Request):
    posts = Post.objects.all()
    context = {'posts': posts}
    rend = render(Request, "/posts/posts_list.html", context)
    return HttpResponse(rend)
