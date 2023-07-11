# my models
from django.shortcuts import render

# my models
from .models import *


# Create your views here.
def post_list(Request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(Request, "./posts/post_list.html", context)


def post_view(Request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comment ": comment,
    }
    return render(Request, "./posts/post_view.html", context)
