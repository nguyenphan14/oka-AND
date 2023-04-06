from django.urls import path

from . import views

urlpatterns = [
    path("send_feedback/", views.send_feedback, name="send_feedback"),
    path("get_feedback/", views.get_feedback, name="get_feedback"),
] 