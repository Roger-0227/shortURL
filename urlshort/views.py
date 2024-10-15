from django.shortcuts import render, get_object_or_404
import random
import string
from urlshort.models import ShortURL
from urlshort.form.url_form import ShortURLForm


def out_home(request):
    return render(request, "out_home.html")


def index(request):
    own_fields = request.GET.get("short_url")
    if request.method == "POST":
        if own_fields == None:
            fields = "".join(random.choices(string.ascii_letters, k=5))
        else:
            fields = own_fields
        form = ShortURLForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.short_url = fields
            form.save()
            return render(request, "pages/show.html", {"form": form})
        else:
            return render("pages/index.hmtl", {"form": form})
    form = ShortURLForm()
    return render(request, "pages/index.html", {"form": form})


def show(request, id):
    url_content = get_object_or_404(ShortURL, id=id)
    return render(request, "pages/show.html", {"form": url_content})
