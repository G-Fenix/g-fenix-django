from django.shortcuts import render

def webdev(request):
    return render(request, 'webdevelopment.html')

def qrmenu(request):
    return render(request, 'qrmenu.html')

def chatbots(request):
    return render(request, 'chatbots.html')

def dataexpertconsultancy(request):
    return render(request, 'dataexpert.html')

def businessanalytics(request):
    return render(request, 'business.html')

def training(request):
    return render(request, 'training.html')

def automation_ai(request):
    return render(request, 'automation_ai.html')