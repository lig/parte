from django import forms


class PostForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput, required=False)
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'span5', 'rows': 1}))


class CommentForm(forms.Form):
    text = forms.CharField()
