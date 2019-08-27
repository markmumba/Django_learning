from django import forms


class NewsLetterForm(forms.Form):
    your_name =forms.CharField(label = 'First Name', max_length = 30)
    mail = forms.EmailField(label = 'Email')