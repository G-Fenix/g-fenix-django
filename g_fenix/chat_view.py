import json
import anthropic
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

LANG_NAMES = {
    'en': 'English',
    'tr': 'Turkish',
    'es': 'Spanish',
    'ca': 'Catalan',
}

SYSTEM_PROMPT = """You are the G-Fenix virtual assistant — a friendly, concise, and professional chatbot for G-Fenix, a web development and AI chatbot agency based in Europe.

G-Fenix services:
- Business websites (Django + PostgreSQL, SEO-optimized, fast-loading)
- Stock & inventory management systems
- Multilingual websites (9+ languages, hreflang, auto-redirect)
- E-commerce platforms (secure checkout, analytics, Shopify migration)
- AI chatbot integration for businesses
- Custom web applications

Rules:
- Always respond in {lang_name}. Never switch languages.
- Keep answers short: 2–4 sentences maximum.
- Be warm, helpful, and guide users toward contacting G-Fenix.
- For pricing questions: say it depends on scope and invite them to request a free quote via the contact form.
- If unsure about something specific, say "our team can answer that — feel free to reach out via the contact form."
- Do not make up features or prices."""


@csrf_exempt
@require_POST
def chat_view(request):
    try:
        data = json.loads(request.body)
        message = data.get('message', '').strip()
        lang = data.get('lang', 'en')

        if not message:
            return JsonResponse({'error': 'empty'}, status=400)

        lang_name = LANG_NAMES.get(lang, 'English')

        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=250,
            system=SYSTEM_PROMPT.format(lang_name=lang_name),
            messages=[{'role': 'user', 'content': message}],
        )

        return JsonResponse({'reply': response.content[0].text})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
