from django.urls import path
from . import views

urlpatterns = [
    path('', views.bizeulasin, name='contact_us_tr'),

]