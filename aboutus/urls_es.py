from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre),
    path('sobre-nosotros', views.sobre),
    path('nuestra-vision', views.ourvisiones),
    path('nuestra-mision', views.ourmissiones),
    path('nuestro-equipo', views.espanyole),
    path('redes-sociales', views.sosyalmedyaes),
]
