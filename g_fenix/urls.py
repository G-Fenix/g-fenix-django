from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from contactus import views as contactus_views
from g_fenix.chat_view import chat_view


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('api/chat/', chat_view, name='chat'),
] + i18n_patterns(
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('services/', include('services.urls'), name='services'),
    path('portfolio/', include('portfolio.urls'), name='portfolio'),
    path('blog/', include('blog.urls'), name='blog'),
    path('about-us/', include('aboutus.urls'), name='aboutus'),
path('contact-us/', include('contactus.urls'), name='contactus'),
    path('legal/', include('legal.urls'), name='legal'),
    path('newsletter/subscribe/', contactus_views.newsletter_subscribe, name='newsletter_subscribe'),
    prefix_default_language=False,
)
