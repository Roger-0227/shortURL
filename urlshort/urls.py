from django.urls import path, include

from . import views

app_name = "urlshort"

urlpatterns = [
    path("", views.out_home, name="out_home"),
    path("index", views.index, name="index"),
    path("show/<int:id>", views.show, name="show"),
]
