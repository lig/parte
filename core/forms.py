from django import forms


class PostForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput, required=False)
    text = forms.CharField()
