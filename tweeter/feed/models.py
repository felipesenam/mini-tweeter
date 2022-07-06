from datetime import datetime
from django.db import models
from users.models import UserImpl
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Tweets(models.Model):
    author = models.ForeignKey(UserImpl, verbose_name=_(
        'Author'), on_delete=models.CASCADE)
    post = models.TextField(verbose_name=_("Post content"), max_length=280)
    published_at = models.DateTimeField(
        verbose_name=_("publication date"), auto_now=True)

    related_tweet = models.ForeignKey(
        "Tweets", verbose_name="Tweet", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
        ordering = ['-published_at']
