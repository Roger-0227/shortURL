from django.urls import path, include

urlpatterns = [
    path("", include("urlshort.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("qr_code/", include("qr_code.urls", namespace="qr_code")),
]
