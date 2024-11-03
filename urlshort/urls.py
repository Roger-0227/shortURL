from django.urls import path

from . import views

app_name = "urlshort"

urlpatterns = [
    path("", views.out_home, name="out_home"),
    path("index", views.index, name="index"),
    path("information", views.information, name="information"),
    path("<str:url>", views.redirect, name="redirect"),
    path("show/<int:id>", views.show, name="show"),
]
