from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactusbg, name='contact_us_bg'),
]