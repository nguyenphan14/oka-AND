from django.urls import path

from . import views

urlpatterns = [
    path("add_item/", views.add_item, name="add_item"),
    path("show_cart/", views.show_cart, name="show_cart"),
    path("delete_cart/", views.delete_cart, name="delete_cart"),
] 