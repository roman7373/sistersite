from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('slug','fullname','author','abstract','file','publish','journal','issn','status',)