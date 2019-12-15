from django import forms

from .models import FileData


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileData
        fields = ('UploadedFile',)
