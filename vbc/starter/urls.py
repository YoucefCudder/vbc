from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import homepage, blog, contact, success, about

app_name = "starter"
urlpatterns = [

    path("", homepage, name="homepage"),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('about/', about, name='about'),

    path("blog/", blog, name="blog"),
    path('', map, name="map"),


]