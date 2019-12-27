from django import forms
from .models import Gmail


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class GmailForm(forms.ModelForm):
    class Meta:
        model=Gmail
        fields=("__all__")