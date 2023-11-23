from django.urls import path
from .views import home, about, contacto, servicios



urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contacto/', contacto, name="contacto"),
    path('servicios/', servicios, name="servicios"),
]
