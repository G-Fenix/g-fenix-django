from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutusbg),
    path('za-nas', views.aboutusbg),
    path('nashata-viziya', views.ourvisionbg),
    path('nashata-misiya', views.ourmissionbg),
    path('nashiyat-ekip', views.bulgaria),
    path('sotsialni-mrezhi', views.socialmediabg),
]
