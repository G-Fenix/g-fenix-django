from django.shortcuts import render

def references(request):
    return render(request, 'references.html')

def user_cases(request):
    return render(request, 'usercases_portfolio.html')
