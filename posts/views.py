
# views file

# importing rest_framework stuff 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# My model
from .models import Post

# My serializer 
from .serializers import PostSerializer


class PostListView(APIView):
    
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    

class PostCreateView(APIView):
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PostDetailView(APIView):
    def get(self, request, pk):
        
        try:
            post = Post.objects.get(pk=pk) 
            # for when: post.pk > length of all posts
        except Post.DoesNotExist:
            return Response('Post Dose Not Exits!!!', status=status.HTTP_404_NOT_FOUND)
        
        serialize = PostSerializer(post)
        return Response(serialize.data)
