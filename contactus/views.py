from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives
from django.utils import translation
from .models import ContactMessage, NewsletterSubscriber

LOGO_URL = 'https://g-fenix.com/static/images/l2no.png'
SITE_URL = 'https://g-fenix.com'

HTML_WRAPPER = """\
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:32px 0;">
  <tr><td align="center">
    <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:8px;overflow:hidden;max-width:600px;">
      <!-- Header -->
      <tr>
        <td style="background:#0a0a0a;padding:24px 40px;">
          <img src="{logo}" alt="G-Fenix" width="120" style="display:block;">
        </td>
      </tr>
      <!-- Body -->
      <tr>
        <td style="padding:40px;color:#1a1a1a;font-size:15px;line-height:1.7;">
          {body}
        </td>
      </tr>
      <!-- Footer -->
      <tr>
        <td style="background:#f9f9f9;padding:20px 40px;border-top:1px solid #e5e5e5;text-align:center;font-size:12px;color:#888;">
          © 2025 G-Fenix &nbsp;|&nbsp;
          <a href="{site}" style="color:#888;text-decoration:none;">g-fenix.com</a> &nbsp;|&nbsp;
          <a href="mailto:hello@g-fenix.com" style="color:#888;text-decoration:none;">hello@g-fenix.com</a>
        </td>
      </tr>
    </table>
  </td></tr>
</table>
</body>
</html>
"""

AUTO_REPLY = {
    'en': {
        'subject': 'Thank you for contacting G-Fenix',
        'text': (
            "Dear {name},\n\n"
            "Thank you for reaching out to G-Fenix. We have received your message and "
            "our team will get back to you within 24 hours on business days.\n\n"
            "In the meantime, feel free to explore our services at https://g-fenix.com\n\n"
            "Best regards,\nG-Fenix Team\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Dear <strong>{name}</strong>,</p>"
            "<p>Thank you for reaching out to G-Fenix. We have received your message and "
            "our team will get back to you <strong>within 24 hours</strong> on business days.</p>"
            "<p>In the meantime, feel free to explore our services:</p>"
            "<p><a href='https://g-fenix.com' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Best regards,<br><strong>G-Fenix Team</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'tr': {
        'subject': 'G-Fenix ile iletişime geçtiğiniz için teşekkürler',
        'text': (
            "Sayın {name},\n\n"
            "G-Fenix ile iletişime geçtiğiniz için teşekkür ederiz. Mesajınızı aldık; "
            "ekibimiz iş günlerinde 24 saat içinde size geri dönüş sağlayacaktır.\n\n"
            "Hizmetlerimizi inceleyebilirsiniz: https://g-fenix.com/tr\n\n"
            "Saygılarımızla,\nG-Fenix Ekibi\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Sayın <strong>{name}</strong>,</p>"
            "<p>G-Fenix ile iletişime geçtiğiniz için teşekkür ederiz. Mesajınızı aldık; "
            "ekibimiz iş günlerinde <strong>24 saat içinde</strong> size geri dönüş sağlayacaktır.</p>"
            "<p>Bu süreçte hizmetlerimizi inceleyebilirsiniz:</p>"
            "<p><a href='https://g-fenix.com/tr' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Saygılarımızla,<br><strong>G-Fenix Ekibi</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'es': {
        'subject': 'Gracias por contactar con G-Fenix',
        'text': (
            "Estimado/a {name},\n\n"
            "Gracias por ponerse en contacto con G-Fenix. Hemos recibido su mensaje y "
            "nuestro equipo le responderá en un plazo de 24 horas en días laborables.\n\n"
            "Explore nuestros servicios en: https://g-fenix.com/es\n\n"
            "Atentamente,\nEl equipo de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Estimado/a <strong>{name}</strong>,</p>"
            "<p>Gracias por ponerse en contacto con G-Fenix. Hemos recibido su mensaje y "
            "nuestro equipo le responderá en un plazo de <strong>24 horas</strong> en días laborables.</p>"
            "<p>Explore nuestros servicios:</p>"
            "<p><a href='https://g-fenix.com/es' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Atentamente,<br><strong>El equipo de G-Fenix</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'ca': {
        'subject': 'Gràcies per contactar amb G-Fenix',
        'text': (
            "Benvolgut/da {name},\n\n"
            "Gràcies per posar-se en contacte amb G-Fenix. Hem rebut el seu missatge i "
            "el nostre equip li respondrà en un termini de 24 hores en dies laborables.\n\n"
            "Explori els nostres serveis: https://g-fenix.com/ca\n\n"
            "Cordialment,\nL'equip de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Benvolgut/da <strong>{name}</strong>,</p>"
            "<p>Gràcies per posar-se en contacte amb G-Fenix. Hem rebut el seu missatge i "
            "el nostre equip li respondrà en un termini de <strong>24 hores</strong> en dies laborables.</p>"
            "<p>Explori els nostres serveis:</p>"
            "<p><a href='https://g-fenix.com/ca' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Cordialment,<br><strong>L'equip de G-Fenix</strong><br>hello@g-fenix.com</p>"
        ),
    },
}

NEWSLETTER_REPLY = {
    'en': {
        'subject': 'G-Fenix will be in touch soon',
        'text': (
            "Hello,\n\nThank you for your interest in G-Fenix! We have received your email and "
            "a member of our team will reach out to you within 2 business hours.\n\n"
            "https://g-fenix.com\n\nBest regards,\nG-Fenix Team\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Hello,</p>"
            "<p>Thank you for your interest in G-Fenix! We have received your email and "
            "a member of our team will reach out to you <strong>within 2 business hours</strong>.</p>"
            "<p><a href='https://g-fenix.com' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Best regards,<br><strong>G-Fenix Team</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'tr': {
        'subject': 'G-Fenix en kısa sürede sizinle iletişime geçecek',
        'text': (
            "Merhaba,\n\nG-Fenix'e gösterdiğiniz ilgi için teşekkür ederiz! E-posta adresinizi aldık; "
            "ekibimizden bir yetkili iş saatlerinde 2 saat içinde sizinle iletişime geçecektir.\n\n"
            "https://g-fenix.com/tr\n\nSaygılarımızla,\nG-Fenix Ekibi\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Merhaba,</p>"
            "<p>G-Fenix'e gösterdiğiniz ilgi için teşekkür ederiz! E-posta adresinizi aldık; "
            "ekibimizden bir yetkili iş saatlerinde <strong>2 saat içinde</strong> sizinle iletişime geçecektir.</p>"
            "<p><a href='https://g-fenix.com/tr' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Saygılarımızla,<br><strong>G-Fenix Ekibi</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'es': {
        'subject': 'G-Fenix se pondrá en contacto pronto',
        'text': (
            "Hola,\n\n¡Gracias por su interés en G-Fenix! Hemos recibido su correo y "
            "un miembro de nuestro equipo se pondrá en contacto en 2 horas hábiles.\n\n"
            "https://g-fenix.com/es\n\nAtentamente,\nEl equipo de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Hola,</p>"
            "<p>¡Gracias por su interés en G-Fenix! Hemos recibido su correo y "
            "un miembro de nuestro equipo se pondrá en contacto con usted en <strong>2 horas hábiles</strong>.</p>"
            "<p><a href='https://g-fenix.com/es' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Atentamente,<br><strong>El equipo de G-Fenix</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'ca': {
        'subject': 'G-Fenix es posarà en contacte aviat',
        'text': (
            "Hola,\n\nGràcies pel seu interès en G-Fenix! Hem rebut el seu correu i "
            "un membre del nostre equip es posarà en contacte en 2 hores hàbils.\n\n"
            "https://g-fenix.com/ca\n\nCordialment,\nL'equip de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Hola,</p>"
            "<p>Gràcies pel seu interès en G-Fenix! Hem rebut el seu correu i "
            "un membre del nostre equip es posarà en contacte en <strong>2 hores hàbils</strong>.</p>"
            "<p><a href='https://g-fenix.com/ca' style='color:#7c3aed;font-weight:bold;'>g-fenix.com</a></p>"
            "<br><p>Cordialment,<br><strong>L'equip de G-Fenix</strong><br>hello@g-fenix.com</p>"
        ),
    },
}


def _send(to_email, subject, text, html_body):
    html = HTML_WRAPPER.format(logo=LOGO_URL, site=SITE_URL, body=html_body)
    msg = EmailMultiAlternatives(
        subject=subject,
        body=text,
        from_email='G-Fenix <hello@g-fenix.com>',
        to=[to_email],
    )
    msg.attach_alternative(html, 'text/html')
    msg.send(fail_silently=True)


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
            first_name=first_name, last_name=last_name,
            email=email, subject=subject, message=message,
        )

        lang = (translation.get_language() or 'en')[:2]
        reply = AUTO_REPLY.get(lang, AUTO_REPLY['en'])
        full_name = f"{first_name} {last_name}".strip() or email

        _send(
            to_email=email,
            subject=reply['subject'],
            text=reply['text'].format(name=full_name),
            html_body=reply['html'].format(name=full_name),
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

        lang = (translation.get_language() or 'en')[:2]
        reply = NEWSLETTER_REPLY.get(lang, NEWSLETTER_REPLY['en'])

        _send(
            to_email=email,
            subject=reply['subject'],
            text=reply['text'],
            html_body=reply['html'],
        )

        return JsonResponse({'status': 'ok'})
    except Exception:
        return JsonResponse({'status': 'error'}, status=500)
