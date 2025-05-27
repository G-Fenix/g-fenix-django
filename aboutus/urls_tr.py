from django.urls import path
from . import views

urlpatterns = [
    path('', views.hakkimizda),
    path('hakkimizda', views.hakkimizda),
    path('vizyonumuz', views.vizyonumuz),
    path('misyonumuz', views.misyonumuz),
    path('ekibimiz', views.ekibimiz),
    path('sosyal-medya', views.sosyalmedya),
]