from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return render(request, 'en/aboutus_en.html')

def hakkimizda(request):
    return render(request, 'tr/aboutus_tr.html')

def sobre(request):
    return render(request, 'es/aboutus_es.html')

def aboutusbg(request):
    return render(request, 'bg/aboutus_bg.html')

def ourvision(request):
    return render(request, 'en/ourvision_en.html')

def ourvisiones(request):
    return render(request, 'es/ourvision_es.html')

def ourvisionbg(request):
    return render(request, 'bg/ourvision_bg.html')

def vizyonumuz(request):
    return render(request, 'tr/ourvision_tr.html')

def ourmission(request):
    return render(request, 'en/ourmission_en.html')

def ourmissiones(request):
    return render(request, 'es/ourmission_es.html')

def ourmissionbg(request):
    return render(request, 'bg/ourmission_bg.html')

def misyonumuz(request):
    return render(request, 'tr/ourmission_tr.html')

def ourteam(request):
    return render(request, 'en/ourteam_en.html')

def ekibimiz(request):
    return render(request, 'tr/ourteam_tr.html')

def ourteames(request):
    return render(request, 'es/ourteam_es.html')

def ourteambg(request):
    return render(request, 'bg/ourteam_bg.html')

def socialmedia(request):
    return render(request, 'en/socialmedia_en.html')

def sosyalmedya(request):
    return render(request, 'tr/socialmedia_tr.html')

def sosyalmedyaes(request):
    return render(request, 'es/sosyalmedia_eses.html')

def socialmediabg(request):
    return render(request, 'bg/socialmedia_bg.html')

def jessica(request):
    return render(request, 'en/jessica_en.html')

def jessicaa(request):
    return render(request, 'tr/jessica_tr.html')

def jessicaaes(request):
    return render(request, 'es/jessica_es.html')

def jessicaabg(request):
    return render(request, 'bg/jessica_bg.html')

def cengizhan(request):
    return render(request, 'en/cengizhan_en.html')

def cengizhann(request):
    return render(request, 'tr/cengizhan_tr.html')

def cengizhannes(request):
    return render(request, 'es/cengizhan_es.html')

def cengizhannbg(request):
    return render(request, 'bg/cengizhan_bg.html')
