from django.urls import path, include

urlpatterns = [
    path("", include("urlshort.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
