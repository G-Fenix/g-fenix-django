from . import views
from django.urls import path

urlpatterns = [
    path('references/', views.references, name='references'),
    path('user-cases/', views.user_cases, name='user_cases'),
]
