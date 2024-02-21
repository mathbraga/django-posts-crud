from rest_framework import generics
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
