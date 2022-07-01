from rest_framework import serializers

from users.models import UserImpl


class UserImplSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImpl
        fields = ['name', 'email', 'birth_date', 'password']
