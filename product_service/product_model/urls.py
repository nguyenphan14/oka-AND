from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_product_data, name='get_product_data'),
]