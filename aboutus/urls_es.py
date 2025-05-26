from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre),
    path('sobre-nosotros', views.sobre),
    path('nuestra-vision', views.ourvisiones),
    path('nuestra-mision', views.ourmissiones),
    path('nuestro-equipo', views.ourteames),
    path('redes-sociales', views.sosyalmedyaes),
    path('nuestro-equipo/jessica/', views.jessicaaes, name='jessicaaes'),
    path('nuestro-equipo/cengizhan/', views.cengizhannes, name='cengizhannes'),
]
