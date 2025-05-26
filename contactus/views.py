from django.shortcuts import render

def contactus(request):
    return render(request, 'en/contactus_en.html')

def bizeulasin(request):
    return render(request, 'tr/contactus_tr.html')

def contactuses(request):
    return render(request, 'es/contactus_es.html')

def contactusbg(request):
    return render(request, 'bg/contactus_bg.html')
