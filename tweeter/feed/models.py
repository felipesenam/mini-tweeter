from django.db import models
from users.models import UserImpl
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Posts(models.Model):
    author = models.ForeignKey(UserImpl, verbose_name=_(
        'Author'), on_delete=models.CASCADE)
    post = models.TextField(verbose_name=_("Post content"), max_length=280)
