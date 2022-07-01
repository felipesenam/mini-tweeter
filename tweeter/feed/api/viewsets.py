from rest_framework import viewsets
from .serializers import PostsSerializer
from feed.models import Posts
from rest_framework.permissions import IsAuthenticated


class PostsViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]

    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
