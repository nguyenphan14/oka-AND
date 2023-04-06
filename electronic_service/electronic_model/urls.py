from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_elec_data, name='get_elec_data'),
]