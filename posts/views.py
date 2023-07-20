# views file

# django imports
from django.http import Http404

# importing rest_framework stuff 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import mixins

# My model
from .models import Post

# My serializer 
from .serializers import PostSerializer

##################### LAZINESS LEVEL 1 #####################

# class PostListView(APIView):
    
#     # Retrieve data
#     def get(self, request):
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         return Response(serializer.data)

#     # Create data
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class PostDetailView(APIView):

#     # get post with pk
#     def get_object(self, pk):
#         try:
#             post = Post.objects.get(pk=pk) 
#             # for when: post.pk > length of all posts
#         except Post.DoesNotExist:
#             raise Http404
#         return post
        

#     # Retrieve data
#     def get(self, request, pk):

#         post = self.get_object(pk)
#         serialize = PostSerializer(post)
#         return Response(serialize.data)
    
#     # Update data
#     def put(self, request, pk):
        
#         post = self.get_object(pk=pk)

#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # delete data
#     def delete(self, request, pk):
#         post = self.get_object(pk=pk)
#         post.delete()
#         return Response("Post has been deleted", status=status.HTTP_204_NO_CONTENT)


##################### LAZINESS LEVEL 2 #####################

# class PostListView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class PostDetailView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, pk, *args, **kwargs):
#         return self.retrieve(request, pk, *args, **kwargs)
    
#     def put(self, request, pk, *args, **kwargs):
#         return self.update(request, pk, *args, **kwargs)

#     def delete(self, request, pk, *args, **kwargs):
#         return self.destroy(request, pk, *args, **kwargs)
    
##################### LAZINESS LEVEL 3 #####################

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# CRUD -- Create, Retrieve, Update, Delete