from django.urls import path
from .views import *
urlpatterns = [
    path("<slug>/", get_products, name="get_products"),
    path('update_price/', update_price, name='update_price'),
]
