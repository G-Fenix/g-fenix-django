from django.shortcuts import render

def ourmission(request):
    return render(request, 'ourmission.html')

def ourvision(request):
    return render(request, 'ourvision.html')

def ourteam(request):
    return render(request, 'ourteam.html')

def jessica_profile(request):
    return render(request, 'jsc.html')

def cengizhan_profile(request):
    return render(request, 'cengizhan.html')
