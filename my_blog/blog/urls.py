from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="starting-page"),
    path("post", views.post_list, name="all-post"),
    path("post/<slug:slug>", views.post_detail, name="slug")
]
