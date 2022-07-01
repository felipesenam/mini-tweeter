from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserImpl


class UserImplCreationForm(UserCreationForm):

    class Meta:
        model = UserImpl
        fields = ('email',)


class UserImplChangeForm(UserChangeForm):

    class Meta:
        model = UserImpl
        fields = ('email',)
