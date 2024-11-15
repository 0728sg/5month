from django.urls import path

from web_shop.urls import urlpatterns
from . import views


urlpatterns = [
    path('', views.products_list_create_api_view),
    path('<int:id>/', views.product_detail_update_destroy_api_view),
]
