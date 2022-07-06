from rest_framework import viewsets

from .serializers import PostsSerializer
from feed.models import Tweets
from rest_framework.response import Response
from rest_framework import mixins
from .permissions import CreateOnlyAuthenticated
from django.utils.translation import gettext as _
from feed.forms import signupForm


class PostsViewset(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    permission_classes = [CreateOnlyAuthenticated, ]

    def create(self, request):
        signupForm(request.data)
        post = Tweets.objects.create(
            author=request.user, post=request.data.get('post'))
        serializer = PostsSerializer(post, many=False)

        return Response(serializer.data)

    def list(self, request):
        queryset = Tweets.objects.all()
        print(request.user)
        if request.user.is_authenticated:
            queryset = queryset.exclude(author=request.user)

        serializer = PostsSerializer(queryset, many=True)

        return Response(serializer.data)
