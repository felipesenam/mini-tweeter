from rest_framework import serializers

from feed.models import Tweets
from users.api.serializers import UserImplPublicSerializer


class PostsSerializer(serializers.ModelSerializer):
    author = UserImplPublicSerializer(read_only=True)

    class Meta:
        model = Tweets
        fields = '__all__'
