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
    return render(request, "starter/homepage.html")


class SuccessView(TemplateView):
    template_name = "starter/success.html"


def blog(request):
    return render(request, 'starter/blog.html')


def map(request):
    return render(request, 'starter/map.html')

def about(request):
    return render(request, 'starter/about.html')


def contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return HttpResponse('Success!')
