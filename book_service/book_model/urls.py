from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_book_data, name='get_book_data'),
]