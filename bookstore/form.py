from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='이름', max_length=100)
    email = forms.EmailField(label='이메일')
