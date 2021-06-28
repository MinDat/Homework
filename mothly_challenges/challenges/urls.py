from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting, name="mainpage"),
    path("<int:month>", views.index),
    path("<str:month>", views.strings, name="month-name")
]