from django.urls import include, path

urlpatterns = [
    path("", include("urlshort.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("qr_code/", include("qr_code.urls", namespace="qr_code")),
]
