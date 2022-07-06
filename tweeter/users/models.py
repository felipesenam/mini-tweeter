
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserImplManager

# Create your models here.


class UserImpl(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=32)
    name = models.CharField(_('name'), max_length=64)
    email = models.EmailField(_('email address'), unique=True)

    birth_date = models.DateField(_('birth date'), null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    objects = UserImplManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
