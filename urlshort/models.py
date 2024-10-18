from django.db import models


class ShortURL(models.Model):
    url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=200, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_enable = models.BooleanField(default=False)

    # def __repr__(self):
    #     return self.short_url
