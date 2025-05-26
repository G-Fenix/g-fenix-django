from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactuses, name='contact_us_es'),
]