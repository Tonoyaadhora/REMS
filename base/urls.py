from django.urls import path, include
from .views import authView, index

urlpatterns = [
 path("", index, name="index"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
]
