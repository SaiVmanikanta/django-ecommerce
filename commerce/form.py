from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(
        max_length=100, required=True, help_text="user_email@email.com")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    your_email = forms.EmailField(
        max_length=100, required=True, help_text="your_email@email.com")
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(max_length=500, widget=forms.Textarea(), required=True)
