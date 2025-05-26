from django.http import HttpResponse
from django.shortcuts import render

def whatwedo(request):
    return render(request, 'en/whatwedo_en.html')

def neyapiyoruz(request):
    return render(request, 'tr/whatwedo_tr.html')

def whatwedoes(request):
    return render(request, 'es/whatwedo_es.html')

def whatwedobg(request):
    return render(request, 'bg/whatwedo_bg.html')

def dataanalysis(request):
    return render(request, 'en/dataanalysis_en.html')

def verianalizi(request):
    return render(request, 'tr/dataanalysis_tr.html')

def dataanalysises(request):
    return render(request, 'es/dataanalysis_es.html')

def dataanalysisbg(request):
    return render(request, 'bg/dataanalysis_bg.html')

def webdevelopment(request):
    return render(request, 'en/webdevelopment_en.html')

def webgelistirme(request):
    return render(request, 'tr/webdevelopment_tr.html')

def webdevelopmentes(request):
    return render(request, 'es/webdevelopment_es.html')

def webdevelopmentbg(request):
    return render(request, 'bg/webdevelopment_bg.html')

def pythondevelopment(request):
    return render(request, 'en/pythondevelopment_en.html')

def pythongelistirme(request):
    return render(request, 'tr/pythondevelopment_tr.html')

def pythondevelopmentes(request):
    return render(request, 'es/pythondevelopment_es.html')

def pythondevelopmentbg(request):
    return render(request, 'bg/pythondevelopment_bg.html')

def ai(request):
    return render(request, 'en/ai_en.html')

def aii(request):
    return render(request, 'tr/ai_tr.html')

def aies(request):
    return render(request, 'es/ai_es.html')

def aibg(request):
    return render(request, 'bg/ai_bg.html')

def usercases(request):
    return render(request, 'en/usercases_en.html')

def kullanici(request):
    return render(request, 'tr/usercases_tr.html')

def usercaseses(request):
    return render(request, 'es/usercases_es.html')

def usercasesbg(request):
    return render(request, 'bg/usercases_bg.html')

def training(request):
    return render(request, 'en/training_en.html')

def egitim(request):
    return render(request, 'tr/training_tr.html')

def traininges(request):
    return render(request, 'es/training_es.html')

def trainingbg(request):
    return render(request, 'bg/training_bg.html')

