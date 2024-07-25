from django.urls import path
from .views import *
urlpatterns = [
    path("<slug>/", get_products, name="get-products"),
]
