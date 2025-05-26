from django.http import HttpResponse
from django.shortcuts import render

def projects(request):
    return render(request, 'en/projects_en.html')

def projeler(request):
    return render(request, 'tr/projects_tr.html')

def projectses(request):
    return render(request, 'es/projects_es.html')

def completedprojects(request):
    return render(request, 'en/completedprojects_en.html')

def tamamlananprojeler(request):
    return render(request, 'tr/completedprojects_tr.html')

def completedprojectses(request):
    return render(request, 'es/completedprojects_es.html')

def completedprojectsbg(request):
    return render(request, 'bg/completedprojects_bg.html')

def ongoingprojects(request):
    return render(request, 'en/ongoingprojects_en.html')

def devamedenprojeler(request):
    return render(request, 'tr/ongoingprojects_tr.html')

def ongoingprojectses(request):
    return render(request, 'es/ongoingprojects_es.html')

def ongoingprojectsbg(request):
    return render(request, 'bg/ongoingprojects_bg.html')

def futureprojects(request):
    return render(request, 'en/futureprojects_en.html')

def gelecekprojeler(request):
    return render(request, 'tr/futureprojects_tr.html')

def futureprojectses(request):
    return render(request, 'es/futureprojects_es.html')

def futureprojectsbg(request):
    return render(request, 'bg/futureprojects_bg.html')

def clientprojects(request):
    return render(request, 'en/clientprojects_en.html')

def musteriprojeleri(request):
    return render(request, 'tr/clientprojects_tr.html')

def clientprojectses(request):
    return render(request, 'es/clientprojects_es.html')

def clientprojectsbg(request):
    return render(request, 'bg/clientprojects_bg.html')