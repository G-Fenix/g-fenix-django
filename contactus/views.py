from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import ContactMessage, NewsletterSubscriber


def contactus(request):
    return render(request, 'contactus.html')

@require_POST
def contact_submit(request):
    try:
        ContactMessage.objects.create(
            first_name = request.POST.get('first_name', '').strip(),
            last_name  = request.POST.get('last_name', '').strip(),
            email      = request.POST.get('email', '').strip(),
            subject    = request.POST.get('subject', '').strip(),
            message    = request.POST.get('message', '').strip(),
        )
        return JsonResponse({'status': 'ok'})
    except Exception:
        return JsonResponse({'status': 'error'}, status=500)


@require_POST
def newsletter_subscribe(request):
    email = request.POST.get('email', '').strip()
    if not email:
        return JsonResponse({'status': 'error'}, status=400)
    try:
        NewsletterSubscriber.objects.get_or_create(email=email)
        return JsonResponse({'status': 'ok'})
    except Exception:
        return JsonResponse({'status': 'error'}, status=500)