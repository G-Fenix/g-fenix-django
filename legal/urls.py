from . import views
from django.urls import path

urlpatterns = [
    path('privacy-policy/', views.privacypolicy, name='privacypolicy'),
    path('terms-of-service/', views.termsofservices, name='termsofservices'),
    path('cookies-policy/', views.cookiepolicy, name='cookiepolicy'),
]
