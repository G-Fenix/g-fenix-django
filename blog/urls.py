from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/', views.blog, name='blog'),
]
