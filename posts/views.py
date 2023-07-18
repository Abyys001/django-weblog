from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import PostSerializer

# my forms
from .forms import PostForm
# my models
from .models import *


# Create your views here.
@api_view(["GET"])
def home(request):

    pk = request.query_params.get('pk')

    if type(pk) != int:
        return Response({"detail": "Post does not exist!!"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        p = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"detail": "Post does not exist!!"}, status=status.HTTP_404_NOT_FOUND)
    json = {
        "Engineer": {
            "fname": "siavash",
            "lname": "drv",
            "nick name":"Abyys01",
            "age": 19,
        }
    }
    serializer = PostSerializer(p)
    return Response(serializer.data)
   

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "./posts/post_list.html", context)


class PostList(generic.ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = 'posts/post_list.html'


def post_detail(request, post_id):
    # try:
    #     post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound("<h1>Post Does NOT Exist!!</h1>")

    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {"post": post, "comment ": comment, }
    return render(request, "./posts/post_detail.html", context)


class PostDetail(generic.DetailView):
    model = Post

    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context["comment"] = Comment.objects.filter(post=kwargs["object"].pk)
        return context


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts')
    else:
        form = PostForm()

    return render(request, './posts/post_create.html', {'form': form})
