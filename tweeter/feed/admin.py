from django.contrib import admin
from .models import Tweets
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'published_at']


admin.site.register(Tweets, PostsAdmin)
