from . import views
from django.urls import path

urlpatterns = [
    path('our-mission/', views.ourmission, name='our_mission'),
    path('our-vision/', views.ourvision, name='our_vision'),
    path('our-team/', views.ourteam, name='our_team'),
    path('team/jessica/', views.jessica_profile, name='jessica_profile'),
    path('team/cengizhan/', views.cengizhan_profile, name='cengizhan_profile'),
]
