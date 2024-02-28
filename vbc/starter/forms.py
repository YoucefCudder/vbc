from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import EmailValidator
from django import forms
from django.http import HttpResponse


class ContactForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Votre nom"}))

    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": " Votre e-mail"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Votre message"})
    )

    # class Meta:
    #     fields = ['nom', 'email', 'message']
    #
    #
    #


