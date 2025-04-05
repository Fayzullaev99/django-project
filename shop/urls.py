from django.urls import path
from shop.views import *

urlpatterns = [
    path("", index, name="index"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
]