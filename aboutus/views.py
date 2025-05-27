from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return render(request, 'aboutus/templates/en/aboutus_en.html')

def hakkimizda(request):
    return render(request, 'aboutus/templates/tr/aboutus_tr.html')

def sobre(request):
    return render(request, 'aboutus/templates/es/aboutus_es.html')

def aboutusbg(request):
    return render(request, 'aboutus/templates/bg/aboutus_bg.html')

def ourvision(request):
    return render(request, 'aboutus/templates/en/ourvision_en.html')

def ourvisiones(request):
    return render(request, 'aboutus/templates/es/ourvision_es.html')

def ourvisionbg(request):
    return render(request, 'aboutus/templates/bg/ourvision_bg.html')

def vizyonumuz(request):
    return render(request, 'aboutus/templates/tr/ourvision_tr.html')

def ourmission(request):
    return render(request, 'aboutus/templates/en/ourmission_en.html')

def ourmissiones(request):
    return render(request, 'aboutus/templates/es/ourmission_es.html')

def ourmissionbg(request):
    return render(request, 'aboutus/templates/bg/ourmission_bg.html')

def misyonumuz(request):
    return render(request, 'aboutus/templates/tr/ourmission_tr.html')

def ourteam(request):
    return render(request, 'aboutus/templates/en/ourteam_en.html')

def turkia(request):
    return render(request, 'aboutus/templates/tr/ourteam_tr.html')

def espanyole(request):
    return render(request, 'aboutus/templates/es/ourteam_es.html')

def bulgaria(request):
    return render(request, 'aboutus/templates/bg/ourteam_bg.html')

def socialmedia(request):
    return render(request, 'aboutus/templates/en/socialmedia_en.html')

def sosyalmedya(request):
    return render(request, 'aboutus/templates/tr/socialmedia_tr.html')

def sosyalmedyaes(request):
    return render(request, 'aboutus/templates/es/sosyalmedia_eses.html')

def socialmediabg(request):
    return render(request, 'aboutus/templates/bg/socialmedia_bg.html')
