from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects),
    path('projects', views.projects),
    path('completed-projects', views.completedprojects),
    path('ongoing-projects', views.ongoingprojects),
    path('future-projects', views.futureprojects),
    path('client-projects', views.clientprojects),
    path('projeler', views.projeler),
    path('tamamlanmis-projeler', views.tamamlananprojeler),
    path('devam-eden-projeler', views.devamedenprojeler),
    path('gelecek-projeler', views.gelecekprojeler),
    path('musteri-projeler', views.musteriprojeleri),
    path('proyectos', views.projectses),
    path('proyectos-completados', views.completedprojectses),
    path('proyectos-en-curso', views.ongoingprojectses),
    path('proyectos-futuros', views.futureprojectses),
    path('proyectos-de-clientes', views.clientprojectses),
    path('zavarsheni-proekti', views.completedprojectsbg),
    path('tekushti-proekti', views.ongoingprojectsbg),
    path('badeshti-proekti', views.futureprojectsbg),
    path('klientski-proekti', views.clientprojectsbg),
    
]