from django import forms


class CreateRecordForm(forms.Form):
    title = forms.CharField(max_length=100)
    body  = forms.CharField()