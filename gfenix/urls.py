"""gfenix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path

def index(request):
    return render(request, 'en/index_en.html')

def index_tr(request):
    return render(request, 'tr/index_tr.html')

def index_es(request):
    return render(request, 'es/index_es.html')

def index_bg(request):
    return render(request, 'bg/index_bg.html')


urlpatterns = [
    path('', index),
    path('tr/', index_tr),
    path('es/', index_es),
    path('bg/', index_bg),
    path('index/', index),
    path('anasayfa/', index_tr),
    path('página de inicio/', index_es),
    path('nachalo/', index_bg),
    path('about-us/', include('aboutus.urls_en')),
    path('blog/', include('blog.urls_en')),
    path('contact-us/', include('contactus.urls_en')),
    path('products/', include('products.urls_en')),
    path('projects/', include('projects.urls')),
    path('what-we-do/', include('whatwedo.urls')),
    path('tr/hakkimizda/', include('aboutus.urls_tr')),
    path('tr/blog/', include('blog.urls_tr')),
    path('tr/bize-ulasin/', include('contactus.urls_tr')),
    path('tr/urunler/', include('products.urls_tr')),
    path('tr/projeler/', include('projects.urls')),
    path('tr/ne-yapiyoruz/', include('whatwedo.urls')),
    path('es/sobre-nosotros/', include('aboutus.urls_es')),
    path('es/blog/', include('blog.urls_es')),
    path('es/contacto/', include('contactus.urls_es')),
    path('es/productos/', include('products.urls_es')),
    path('es/proyectos/', include('projects.urls')),
    path('es/que-hacemos/', include('whatwedo.urls')),
    path('bg/za-nas/', include('aboutus.urls_bg')),
    path('bg/blog/', include('blog.urls_bg')),
    path('bg/kontakt/', include('contactus.urls_bg')),
    path('bg/produkti/', include('products.urls_bg')),
    path('bg/proekti/', include('projects.urls')),
    path('bg/kakvo-pravim/', include('whatwedo.urls')),
    path('admin/', admin.site.urls),
]
