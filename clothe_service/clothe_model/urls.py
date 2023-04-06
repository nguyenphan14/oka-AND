from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_clothe_data, name='get_clothe_data'),
]