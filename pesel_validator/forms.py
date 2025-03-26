from django import forms


class UploadPeselForm(forms.Form):
    pesel = forms.CharField(max_length=11, min_length=11)