from django.http import HttpResponse
from django.shortcuts import render

def products(request):
    return render(request, 'en/products_en.html')

def urunler(request):
    return render(request, 'tr/products_tr.html')

def productses(request):
    return render(request, 'es/products_es.html')

def productsbg(request):
    return render(request, 'bg/products_bg.html')
