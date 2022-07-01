from rest_framework import mixins, viewsets

from users.models import UserImpl

from .serializers import UserImplSerializer


class UserImplViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = UserImplSerializer
    # queryset = UserImpl.objects.all()
