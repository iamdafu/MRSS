from django import forms

class SearchWordForm(forms.Form):
    search_word = forms.CharField(max_length=200)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
