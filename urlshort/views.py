from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
import random
import string
from urlshort.models import ShortURL
from urlshort.form.url_form import ShortURLForm
from django.contrib import messages
import requests
from bs4 import BeautifulSoup


def out_home(request):
    return render(request, "out_home.html")


def index(request):
    if request.method == "POST":
        is_enable = request.POST.get("is_enable")
        fields = random_unique(request.POST.get("short_url"))
        form = ShortURLForm(request.POST)
        if form.is_valid() and fields:
            form = form.save(commit=False)
            form.short_url = f"http://54.95.125.250:8000/{fields}"
            form.is_enable = bool(is_enable)
            form.save()
            messages.success(request, "短網址完成")
            return render(request, "pages/show.html", {"form": form})
        messages.error(request, "請重新輸入/自動產生")
        return render(request, "pages/index.html", {"form": form})
    form = ShortURLForm()
    return render(request, "pages/index.html", {"form": form})


def show(request, id):
    url_content = get_object_or_404(ShortURL, id=id)
    return render(request, "pages/show.html", {"form": url_content})


def redirect(request, url):
    breakpoint()
    if request.GET:
        url_content = ShortURL.objects.get(short_url=f"http://54.95.125.250:8000/{url}")
        url = url_content.url
        return HttpResponseRedirect(url)
    return render(request, "pages/index.html")


def random_unique(str_url):
    short_url = f"http://54.95.125.250:8000/{str_url}"
    if not ShortURL.objects.filter(short_url=short_url).exists():
        if str_url == None:
            radom_field = "".join(random.choices(string.ascii_letters, k=6))
        else:
            radom_field = str_url
        return radom_field
    return False


def information(request):
    form = ShortURLForm(request.POST)
    url = request.POST.get("url")
    if url:
        web = requests.get(url)
        web.encoding = "utf-8"
        soup = BeautifulSoup(web.text, "html.parser")
        title = soup.title.get_text()
        description = soup.find("meta", attrs={"name": "description"})["content"]
        # breakpoint()
        return render(
            request,
            "pages/index.html",
            {
                "web_content": f"{title}\n{description}",
                "form": ShortURLForm(initial={"url": url}),
                "url": url,
            },
        )
    return render(request, "pages/index.html", {"form": form})
