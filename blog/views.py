from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    return render(request, 'en/blog_en.html')

def blog_tr(request):
    return render(request, 'tr/blog_tr.html')

def bloges(request):
    return render(request, 'es/blog_es.html')

def blogbg(request):
    return render(request, 'bg/blog_bg.html')

