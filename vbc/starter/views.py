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
    form = ContactForm
    return render(request, "starter/homepage.html", {"form": form})


class SuccessView(TemplateView):
    template_name = "starter/success.html"


class ContactView(FormView):
    template_name = "starter/contact.html"
    form_class = ContactForm
    success_url = "starter/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm
        return context

    def form_valid(self, form):
        if self.request.method == "POST":
            form = ContactForm(self.request.POST)
            if form.is_valid():
                nom = form.cleaned_data["nom"]
                email = form.cleaned_data["email"]
                message = form.cleaned_data["message"]
                full_message = f"""
                               Received message below from {nom}, {email}
                               ________________________
    
    
                               {message}
                               """

                send_mail(
                    subject="Received contact form submission",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.NOTIFY_EMAIL],

                )

                messages.success(self.request, "Votre message a bien été envoyé.")
                return redirect("starter:success")

            else:
                messages.error(self.request, "Votre message n'a pas été envoyé.")
                return redirect("starter:contact")

        else:
            messages.error(self.request, "Votre message n'a pas été envoyé.")
            return redirect("starter:contact")


def instagram_feed():
    pass


