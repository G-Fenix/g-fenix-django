from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutus),
    path('about-us', views.aboutus),
    path('our-vision', views.ourvision),
    path('our-mission', views.ourmission),
    path('our-team', views.aourteam),
    path('social-media', views.socialmedia),
]
