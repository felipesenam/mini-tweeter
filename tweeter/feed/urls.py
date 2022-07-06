from .views import *
from django.urls import path

urlpatterns = [
    path('', feedView.as_view(), name="feed"),

    path('register/', registerView.as_view(), name="register"),
    path('login/', loginView.as_view(), name="login"),
    path('logout/', logoutUser.as_view(), name="logout"),
]
