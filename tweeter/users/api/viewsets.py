from rest_framework import mixins, viewsets
from rest_framework.response import Response

from users.models import UserImpl

from .serializers import UserImplSerializer


class UserImplViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = UserImplSerializer

    def list(self, request):
        try:
            queryset = UserImpl.objects.get(id=request.user.id)
            serializer = UserImplSerializer(queryset, many=False)
            return Response(serializer.data)
        except:
            return Response(status=401)
