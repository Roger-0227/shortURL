from django import forms

from urlshort.models import ShortURL


class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ["url", "short_url", "note", "is_enable"]

        widgets = {
            "url": forms.URLInput(
                attrs={
                    "class": "input input-bordered flex items-center gap-2 opacity-70 join-item w-full",
                    "name": "url",
                    "placeholder": "http://www.example.com",
                    "x-model": "url",
                },
            ),
            "short_url": forms.TextInput(
                attrs={
                    "class": "input input-bordered flex items-center gap-2 opacity-70 join-item w-full",
                    "name": "short_url",
                    "placeholder": "可自行填寫或自動產生",
                },
            ),
            "note": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full opacity-70",
                    "name": "note",
                    "placeholder": "備註",
                },
            ),
        }
