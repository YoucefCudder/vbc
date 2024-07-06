from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from config import settings


def homepage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            send_mail(subject="contact boxe site internet",
                      message=f"{message} \n de la part de {nom}, email : {email}", from_email=email,
                      recipient_list=["you.aouali@gmail.com", email])

            messages.add_message(request, messages.INFO,
                                 "Email envoyé, je réponds au plus vite :) Vous avez reçu une copie de l'email.")

        else:

            messages.add_message(request, messages.INFO,
                             "Erreur dans l'envoi")

        return redirect("starter:homepage")

    else:
        form = ContactForm()

    return render(request, "starter/homepage.html", context={"form": form})


class SuccessView(TemplateView):
    template_name = "starter/success.html"


def blog(request):
    return render(request, 'starter/blog.html')


def map(request):
    return render(request, 'starter/map.html')


def about(request):
    return render(request, 'starter/about.html')


def faq(request):
    return render(request, 'starter/faq.html')


def success(request):
    return HttpResponse('Success!')
