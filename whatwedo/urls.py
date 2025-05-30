from django.urls import path
from . import views

urlpatterns = [
    path('', views.whatwedo),
    path('what-we-do', views.whatwedo),
    path('data-analysis', views.dataanalysis),
    path('web-development', views.webdevelopment),
    path('python-development', views.pythondevelopment),
    path('ai', views.ai),
    path('usercases', views.usercases),
    path('training', views.training),
    path('ne-yapiyoruz', views.neyapiyoruz),
    path('veri-analiz', views.verianalizi),
    path('web-gelistirme', views.webgelistirme),
    path('python-gelistirme', views.pythongelistirme),
    path('yapay-zeka-uygulamalari', views.aii),
    path('kullanici-durumlari', views.kullanici),
    path('egitim', views.egitim),
    path('que-hacemos', views.whatwedoes),
    path('analisis-de-datos', views.dataanalysises),
    path('desarrollo-web', views.webdevelopmentes),
    path('desarrollo-python', views.pythondevelopmentes),
    path('ia', views.aies),
    path('casos-de-usuario', views.usercaseses),
    path('formacion', views.traininges),
    path('kakvo-pravim', views.whatwedobg),
    path('analiz-na-danni', views.dataanalysisbg),
    path('web-razrabotka', views.webdevelopmentbg),
    path('python-razrabotka', views.pythondevelopmentbg),
    path('izkustven-intellekt', views.aibg),
    path('primeri', views.usercasesbg),
    path('obuchenie', views.trainingbg),
]