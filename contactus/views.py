from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives
from .models import ContactMessage, NewsletterSubscriber

LOGO_URL = 'https://g-fenix.com/static/images/l1ye.png'
SITE_URL  = 'https://g-fenix.com'

HTML_WRAPPER = """\
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:32px 0;">
  <tr><td align="center">
    <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:8px;overflow:hidden;max-width:600px;">
      <tr>
        <td style="background:#0a0a0a;padding:24px 40px;">
          <img src="{logo}" alt="G-Fenix" width="120" style="display:block;">
        </td>
      </tr>
      <tr>
        <td style="padding:40px;color:#1a1a1a;font-size:15px;line-height:1.7;">
          {body}
        </td>
      </tr>
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
            "our team will get back to you within 24 hours on business days. "
            "Messages sent over the weekend will be answered on Monday.\n\n"
            "While you wait, feel free to explore our services — from web development "
            "and AI chatbots to data consultancy and automation:\n"
            "https://g-fenix.com\n\n"
            "Best regards,\nG-Fenix Team\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Dear <strong>{name}</strong>,</p>"
            "<p>Thank you for reaching out to G-Fenix. We have received your message and "
            "our team will get back to you <strong>within 24 hours</strong> on business days. "
            "Messages sent over the weekend will be answered on <strong>Monday</strong>.</p>"
            "<p>While you wait, feel free to explore what we offer — from web development "
            "and AI chatbots to data consultancy and smart automation:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>Explore G-Fenix</a></p>"
            "<br><p>Best regards,<br><strong>G-Fenix Team</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'tr': {
        'subject': 'G-Fenix ile iletişime geçtiğiniz için teşekkürler',
        'text': (
            "Sayın {name},\n\n"
            "G-Fenix ile iletişime geçtiğiniz için teşekkür ederiz. Mesajınızı aldık; "
            "ekibimiz iş günlerinde 24 saat içinde size geri dönüş sağlayacaktır. "
            "Hafta sonu gönderilen mesajlar Pazartesi günü yanıtlanacaktır.\n\n"
            "Bu süreçte web geliştirme, yapay zeka sohbet botları, veri danışmanlığı "
            "ve otomasyon hizmetlerimizi inceleyebilirsiniz:\n"
            "https://g-fenix.com/tr\n\n"
            "Saygılarımızla,\nG-Fenix Ekibi\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Sayın <strong>{name}</strong>,</p>"
            "<p>G-Fenix ile iletişime geçtiğiniz için teşekkür ederiz. Mesajınızı aldık; "
            "ekibimiz iş günlerinde <strong>24 saat içinde</strong> size geri dönüş sağlayacaktır. "
            "Hafta sonu gönderilen mesajlar <strong>Pazartesi</strong> günü yanıtlanacaktır.</p>"
            "<p>Bu süreçte web geliştirme, yapay zeka sohbet botları, veri danışmanlığı "
            "ve otomasyon hizmetlerimizi inceleyebilirsiniz:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com/tr' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>G-Fenix'i Keşfet</a></p>"
            "<br><p>Saygılarımızla,<br><strong>G-Fenix Ekibi</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'es': {
        'subject': 'Gracias por contactar con G-Fenix',
        'text': (
            "Estimado/a {name},\n\n"
            "Gracias por ponerse en contacto con G-Fenix. Hemos recibido su mensaje y "
            "nuestro equipo le responderá en un plazo de 24 horas en días laborables. "
            "Los mensajes enviados durante el fin de semana serán respondidos el lunes.\n\n"
            "Mientras tanto, le invitamos a explorar nuestros servicios — desde desarrollo web "
            "e inteligencia artificial hasta consultoría de datos y automatización:\n"
            "https://g-fenix.com/es\n\n"
            "Atentamente,\nEl equipo de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Estimado/a <strong>{name}</strong>,</p>"
            "<p>Gracias por ponerse en contacto con G-Fenix. Hemos recibido su mensaje y "
            "nuestro equipo le responderá en un plazo de <strong>24 horas</strong> en días laborables. "
            "Los mensajes enviados durante el fin de semana serán respondidos el <strong>lunes</strong>.</p>"
            "<p>Mientras tanto, le invitamos a explorar nuestros servicios — desde desarrollo web "
            "e IA hasta consultoría de datos y automatización inteligente:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com/es' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>Explorar G-Fenix</a></p>"
            "<br><p>Atentamente,<br><strong>El equipo de G-Fenix</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'ca': {
        'subject': 'Gràcies per contactar amb G-Fenix',
        'text': (
            "Benvolgut/da {name},\n\n"
            "Gràcies per posar-se en contacte amb G-Fenix. Hem rebut el seu missatge i "
            "el nostre equip li respondrà en un termini de 24 hores en dies laborables. "
            "Els missatges enviats durant el cap de setmana es respondran el dilluns.\n\n"
            "Mentrestant, l'invitem a explorar els nostres serveis — des del desenvolupament web "
            "i la IA fins a la consultoria de dades i l'automatització:\n"
            "https://g-fenix.com/ca\n\n"
            "Cordialment,\nL'equip de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Benvolgut/da <strong>{name}</strong>,</p>"
            "<p>Gràcies per posar-se en contacte amb G-Fenix. Hem rebut el seu missatge i "
            "el nostre equip li respondrà en un termini de <strong>24 hores</strong> en dies laborables. "
            "Els missatges enviats durant el cap de setmana es respondran el <strong>dilluns</strong>.</p>"
            "<p>Mentrestant, l'invitem a explorar els nostres serveis — des del desenvolupament web "
            "i la IA fins a la consultoria de dades i l'automatització intel·ligent:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com/ca' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>Explorar G-Fenix</a></p>"
            "<br><p>Cordialment,<br><strong>L'equip de G-Fenix</strong><br>hello@g-fenix.com</p>"
        ),
    },
}

NEWSLETTER_REPLY = {
    'en': {
        'subject': 'G-Fenix will be in touch soon',
        'text': (
            "Hello,\n\nThank you for your interest in G-Fenix! We have received your email and "
            "our team will reach out to you within 24 hours on business days. "
            "Messages sent over the weekend will be answered on Monday.\n\n"
            "In the meantime, explore our full range of services:\n"
            "https://g-fenix.com\n\nBest regards,\nG-Fenix Team\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Hello,</p>"
            "<p>Thank you for your interest in G-Fenix! We have received your email and "
            "our team will reach out to you <strong>within 24 hours</strong> on business days. "
            "Messages sent over the weekend will be answered on <strong>Monday</strong>.</p>"
            "<p>In the meantime, explore our full range of services — web development, "
            "AI chatbots, data consultancy and smart automation:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>Explore G-Fenix</a></p>"
            "<br><p>Best regards,<br><strong>G-Fenix Team</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'tr': {
        'subject': 'G-Fenix en kısa sürede sizinle iletişime geçecek',
        'text': (
            "Merhaba,\n\nG-Fenix'e gösterdiğiniz ilgi için teşekkür ederiz! E-posta adresinizi aldık; "
            "ekibimiz iş günlerinde 24 saat içinde sizinle iletişime geçecektir. "
            "Hafta sonu gönderilen mesajlar Pazartesi günü yanıtlanacaktır.\n\n"
            "Bu süreçte hizmetlerimizi inceleyebilirsiniz:\n"
            "https://g-fenix.com/tr\n\nSaygılarımızla,\nG-Fenix Ekibi\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Merhaba,</p>"
            "<p>G-Fenix'e gösterdiğiniz ilgi için teşekkür ederiz! E-posta adresinizi aldık; "
            "ekibimiz iş günlerinde <strong>24 saat içinde</strong> sizinle iletişime geçecektir. "
            "Hafta sonu gönderilen mesajlar <strong>Pazartesi</strong> günü yanıtlanacaktır.</p>"
            "<p>Bu süreçte web geliştirme, yapay zeka sohbet botları, veri danışmanlığı "
            "ve otomasyon hizmetlerimizi inceleyebilirsiniz:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com/tr' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>G-Fenix'i Keşfet</a></p>"
            "<br><p>Saygılarımızla,<br><strong>G-Fenix Ekibi</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'es': {
        'subject': 'G-Fenix se pondrá en contacto pronto',
        'text': (
            "Hola,\n\n¡Gracias por su interés en G-Fenix! Hemos recibido su correo y "
            "nuestro equipo se pondrá en contacto en 24 horas en días laborables. "
            "Los mensajes del fin de semana se responden el lunes.\n\n"
            "Explore nuestros servicios:\nhttps://g-fenix.com/es\n\n"
            "Atentamente,\nEl equipo de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Hola,</p>"
            "<p>¡Gracias por su interés en G-Fenix! Hemos recibido su correo y "
            "nuestro equipo se pondrá en contacto con usted en <strong>24 horas</strong> en días laborables. "
            "Los mensajes enviados el fin de semana se responden el <strong>lunes</strong>.</p>"
            "<p>Explore nuestra gama completa de servicios — desarrollo web, IA, "
            "consultoría de datos y automatización:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com/es' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>Explorar G-Fenix</a></p>"
            "<br><p>Atentamente,<br><strong>El equipo de G-Fenix</strong><br>hello@g-fenix.com</p>"
        ),
    },
    'ca': {
        'subject': 'G-Fenix es posarà en contacte aviat',
        'text': (
            "Hola,\n\nGràcies pel seu interès en G-Fenix! Hem rebut el seu correu i "
            "el nostre equip es posarà en contacte en 24 hores en dies laborables. "
            "Els missatges del cap de setmana es responen el dilluns.\n\n"
            "Explori els nostres serveis:\nhttps://g-fenix.com/ca\n\n"
            "Cordialment,\nL'equip de G-Fenix\nhello@g-fenix.com"
        ),
        'html': (
            "<p>Hola,</p>"
            "<p>Gràcies pel seu interès en G-Fenix! Hem rebut el seu correu i "
            "el nostre equip es posarà en contacte en <strong>24 hores</strong> en dies laborables. "
            "Els missatges del cap de setmana es responen el <strong>dilluns</strong>.</p>"
            "<p>Explori la nostra oferta completa de serveis — desenvolupament web, IA, "
            "consultoria de dades i automatització:</p>"
            "<p style='margin:20px 0;'>"
            "<a href='https://g-fenix.com/ca' style='background:#7c3aed;color:#fff;padding:12px 24px;"
            "border-radius:6px;text-decoration:none;font-weight:bold;'>Explorar G-Fenix</a></p>"
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


def _lang(request):
    code = getattr(request, 'LANGUAGE_CODE', 'en') or 'en'
    return code[:2]


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

        lang  = _lang(request)
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

        lang  = _lang(request)
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
