from django.urls import path, include
from .views import *
urlpatterns = [
    path('login/', login_page, name = "Login page"),
    path('register/', register_page, name = "Register page"),
]

