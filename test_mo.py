import gettext, os
base = r"c:\Users\cengi\Desktop\gfenixfinal\locale"
for lang in ["tr", "es", "ca"]:
    mo = os.path.join(base, lang, "LC_MESSAGES", "django.mo")
    try:
        with open(mo, "rb") as f:
            t = gettext.GNUTranslations(f)
        msg1 = t.gettext("QR Business Card")
        msg2 = t.gettext("Services")
        msg3 = t.gettext("Contact Us")
        print(f"{lang}: OK ({len(t._catalog)} entries)")
        print(f"  Services        -> {msg2}")
        print(f"  Contact Us      -> {msg3}")
        print(f"  QR Business Card-> {msg1}")
    except Exception as e:
        print(f"{lang}: ERROR - {e}")
