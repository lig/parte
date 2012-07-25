from django import forms


class PostForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput)
    text = forms.CharField(widget=forms.Textarea)
