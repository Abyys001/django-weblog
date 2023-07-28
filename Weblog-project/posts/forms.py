# forms python file

from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    is_enable = forms.BooleanField()
    published_date = forms.DateField()
