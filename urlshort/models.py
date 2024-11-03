from django.db import models
from django.utils import timezone


class User(models.Model):
    email = models.EmailField()
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=False, default="")
    address = models.CharField(max_length=100, blank=False, null=False, default="")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username}"


class ShortURL(models.Model):
    url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=200, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_enable = models.BooleanField(default=False)

    # def __repr__(self):
    #     return self.short_url
