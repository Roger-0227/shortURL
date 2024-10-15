from django.shortcuts import render


def out_home(request):
    return render(request, "out_home.html")


def home(request):
    return render(request, "pages/home.html")
