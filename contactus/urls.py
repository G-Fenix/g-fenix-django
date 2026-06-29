from . import views
from django.urls import path

urlpatterns = [
    path('', views.contactus, name='contact_us'),
    path('contact-us/', views.contactus, name='contact_us'),
    path('contact-us/submit/', views.contact_submit, name='contact_submit'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
