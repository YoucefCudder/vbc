from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import homepage, ContactView, SuccessView

app_name = "starter"
urlpatterns = [

    path("", homepage, name="homepage"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),


]#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)