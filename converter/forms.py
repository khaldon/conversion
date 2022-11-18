from django import forms


class HtmlToPdfForm(forms.Form):
    file = forms.FileField()
