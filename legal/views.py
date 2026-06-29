from django.shortcuts import render

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def termsofservices(request):
    return render(request, 'termsofservices.html')

def cookiepolicy(request):
    return render(request, 'cookiepolicy.html')
