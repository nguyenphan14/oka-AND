from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_req, name='registration_req'),

]