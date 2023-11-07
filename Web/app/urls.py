from django.urls import path
from .views import home, contacto, servicios

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('servicios/', servicios, name="servicios"),
]
