#-*-coding:utf-8-*-
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)


class uploadForm(forms.Form):
    description = forms.CharField(max_length=90)
    file = forms.FileField()
#     fields = ('Description', 'Documento')

