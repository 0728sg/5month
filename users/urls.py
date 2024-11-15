from django.urls import path

from products.urls import urlpatterns
from . import views

urlpatterns = [
    path('register/', views.register_api_view),
    path('authorization/', views.authorization_api_view),
]