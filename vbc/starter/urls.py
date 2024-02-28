from django.urls import path

from .views import homepage, ContactView, SuccessView

app_name = "starter"
urlpatterns = [

    path("", homepage, name="homepage"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),


]