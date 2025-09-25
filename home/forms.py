from django import forms
from .models import Todo


class CreateRecordForm(forms.Form):
    title = forms.CharField(max_length=100)
    body  = forms.CharField()

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body']