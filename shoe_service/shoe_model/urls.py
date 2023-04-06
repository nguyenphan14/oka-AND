from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_shoe_data, name='get_shoe_data'),
]