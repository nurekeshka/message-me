
from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your name here'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Please enter what you want to message...'}))
