from django import forms

class postForm(forms.Form):
    message = forms.CharField(required = True, label = "Your Message")
