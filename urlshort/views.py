from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
import random
import string
from urlshort.models import ShortURL
from urlshort.form.url_form import ShortURLForm


def out_home(request):
    return render(request, "out_home.html")


def index(request):
    if request.method == "POST":
        fields = radom_unique(request.POST.get("short_url"))
        form = ShortURLForm(request.POST)
        if form.is_valid() and fields:
            form = form.save(commit=False)
            form.short_url = fields
            form.save()
            return render(request, "pages/show.html", {"form": form})
        return render(request, "pages/index.html", {"form": form})
    form = ShortURLForm()
    return render(request, "pages/index.html", {"form": form})


def show(request, id):
    url_content = get_object_or_404(ShortURL, id=id)
    return render(request, "pages/show.html", {"form": url_content})


def redirect(request, url):
    url_content = ShortURL.objects.get(short_url=url)
    url = url_content.url
    return HttpResponseRedirect(url)


def radom_unique(str_url):
    if not ShortURL.objects.filter(short_url=str_url).exists():
        if str_url == None:
            radom_field = "".join(random.choices(string.ascii_letters, k=6))
        else:
            radom_field = str_url
        return radom_field
    return False
