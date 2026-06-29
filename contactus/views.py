from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.utils import translation
from .models import ContactMessage, NewsletterSubscriber

AUTO_REPLY = {
    'en': {
        'subject': 'Thank you for contacting G-Fenix',
        'body': (
            "Dear {name},\n\n"
            "Thank you for reaching out to G-Fenix. We have received your message and "
            "our team will get back to you within 24 hours on business days.\n\n"
            "In the meantime, feel free to explore our services at https://g-fenix.com\n\n"
            "Best regards,\n"
            "G-Fenix Team\n"
            "hello@g-fenix.com"
        ),
    },
    'tr': {
        'subject': 'G-Fenix ile iletişime geçtiğiniz için teşekkürler',
        'body': (
            "Sayın {name},\n\n"
            "G-Fenix ile iletişime geçtiğiniz için teşekkür ederiz. Mesajınızı aldık; "
            "ekibimiz iş günlerinde 24 saat içinde size geri dönüş sağlayacaktır.\n\n"
            "Bu süreçte hizmetlerimizi inceleyebilirsiniz: https://g-fenix.com/tr\n\n"
            "Saygılarımızla,\n"
            "G-Fenix Ekibi\n"
            "hello@g-fenix.com"
        ),
    },
    'es': {
        'subject': 'Gracias por contactar con G-Fenix',
        'body': (
            "Estimado/a {name},\n\n"
            "Gracias por ponerse en contacto con G-Fenix. Hemos recibido su mensaje y "
            "nuestro equipo le responderá en un plazo de 24 horas en días laborables.\n\n"
            "Mientras tanto, puede explorar nuestros servicios en: https://g-fenix.com/es\n\n"
            "Atentamente,\n"
            "El equipo de G-Fenix\n"
            "hello@g-fenix.com"
        ),
    },
    'ca': {
        'subject': 'Gràcies per contactar amb G-Fenix',
        'body': (
            "Benvolgut/da {name},\n\n"
            "Gràcies per posar-se en contacte amb G-Fenix. Hem rebut el seu missatge i "
            "el nostre equip li respondrà en un termini de 24 hores en dies laborables.\n\n"
            "Mentrestant, pot explorar els nostres serveis a: https://g-fenix.com/ca\n\n"
            "Cordialment,\n"
            "L'equip de G-Fenix\n"
            "hello@g-fenix.com"
        ),
    },
}


def contactus(request):
    return render(request, 'contactus.html')

@require_POST
def contact_submit(request):
    try:
        first_name = request.POST.get('first_name', '').strip()
        last_name  = request.POST.get('last_name', '').strip()
        email      = request.POST.get('email', '').strip()
        subject    = request.POST.get('subject', '').strip()
        message    = request.POST.get('message', '').strip()

        ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message,
        )

        lang = translation.get_language() or 'en'
        lang = lang[:2] if lang else 'en'
        reply = AUTO_REPLY.get(lang, AUTO_REPLY['en'])
        full_name = f"{first_name} {last_name}".strip() or email

        send_mail(
            subject=reply['subject'],
            message=reply['body'].format(name=full_name),
            from_email='G-Fenix <hello@g-fenix.com>',
            recipient_list=[email],
            fail_silently=True,
        )

        return JsonResponse({'status': 'ok'})
    except Exception:
        return JsonResponse({'status': 'error'}, status=500)


NEWSLETTER_REPLY = {
    'en': {
        'subject': 'G-Fenix will be in touch soon',
        'body': (
            "Hello,\n\n"
            "Thank you for your interest in G-Fenix! We have received your email and "
            "a member of our team will reach out to you within 2 business hours.\n\n"
            "In the meantime, feel free to explore our services:\n"
            "https://g-fenix.com\n\n"
            "Best regards,\n"
            "G-Fenix Team\n"
            "hello@g-fenix.com"
        ),
    },
    'tr': {
        'subject': 'G-Fenix en kısa sürede sizinle iletişime geçecek',
        'body': (
            "Merhaba,\n\n"
            "G-Fenix'e gösterdiğiniz ilgi için teşekkür ederiz! E-posta adresinizi aldık; "
            "ekibimizden bir yetkili iş saatlerinde 2 saat içinde sizinle iletişime geçecektir.\n\n"
            "Bu süreçte hizmetlerimizi inceleyebilirsiniz:\n"
            "https://g-fenix.com/tr\n\n"
            "Saygılarımızla,\n"
            "G-Fenix Ekibi\n"
            "hello@g-fenix.com"
        ),
    },
    'es': {
        'subject': 'G-Fenix se pondrá en contacto pronto',
        'body': (
            "Hola,\n\n"
            "¡Gracias por su interés en G-Fenix! Hemos recibido su correo electrónico y "
            "un miembro de nuestro equipo se pondrá en contacto con usted en un plazo de "
            "2 horas hábiles.\n\n"
            "Mientras tanto, puede explorar nuestros servicios:\n"
            "https://g-fenix.com/es\n\n"
            "Atentamente,\n"
            "El equipo de G-Fenix\n"
            "hello@g-fenix.com"
        ),
    },
    'ca': {
        'subject': 'G-Fenix es posarà en contacte aviat',
        'body': (
            "Hola,\n\n"
            "Gràcies pel seu interès en G-Fenix! Hem rebut el seu correu electrònic i "
            "un membre del nostre equip es posarà en contacte amb vostè en un termini de "
            "2 hores hàbils.\n\n"
            "Mentrestant, pot explorar els nostres serveis:\n"
            "https://g-fenix.com/ca\n\n"
            "Cordialment,\n"
            "L'equip de G-Fenix\n"
            "hello@g-fenix.com"
        ),
    },
}


@require_POST
def newsletter_subscribe(request):
    email = request.POST.get('email', '').strip()
    if not email:
        return JsonResponse({'status': 'error'}, status=400)
    try:
        NewsletterSubscriber.objects.get_or_create(email=email)

        lang = translation.get_language() or 'en'
        lang = lang[:2]
        reply = NEWSLETTER_REPLY.get(lang, NEWSLETTER_REPLY['en'])

        send_mail(
            subject=reply['subject'],
            message=reply['body'],
            from_email='G-Fenix <hello@g-fenix.com>',
            recipient_list=[email],
            fail_silently=True,
        )

        return JsonResponse({'status': 'ok'})
    except Exception:
        return JsonResponse({'status': 'error'}, status=500)