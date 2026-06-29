from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.timezone import now
from contactus import views as contactus_views
from g_fenix.chat_view import chat_view


def index(request):
    return render(request, 'index.html')


def sitemap_view(request):
    base = 'https://g-fenix.com'
    today = now().date().isoformat()
    pages = [
        ('/', 'weekly', '1.0'),
        ('/services/build/web-development/', 'monthly', '0.9'),
        ('/services/build/qr-menu/', 'monthly', '0.8'),
        ('/services/build/chatbots/', 'monthly', '0.8'),
        ('/services/data/data-expert-consultancy/', 'monthly', '0.9'),
        ('/services/data/training/', 'monthly', '0.8'),
        ('/services/data/automation-ai/', 'monthly', '0.8'),
        ('/portfolio/references/', 'monthly', '0.7'),
        ('/portfolio/user-cases/', 'monthly', '0.7'),
        ('/about-us/our-team/', 'monthly', '0.6'),
        ('/about-us/our-vision/', 'monthly', '0.5'),
        ('/about-us/our-mission/', 'monthly', '0.5'),
        ('/blog/', 'weekly', '0.6'),
        ('/contact-us/', 'monthly', '0.7'),
    ]
    urls = [{'path': p, 'lastmod': today, 'freq': f, 'priority': pr} for p, f, pr in pages]
    content = render(request, 'sitemap.xml', {'urls': urls, 'base': base})
    return HttpResponse(content.content, content_type='application/xml')


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('api/chat/', chat_view, name='chat'),
    path('sitemap.xml', sitemap_view, name='sitemap'),
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
