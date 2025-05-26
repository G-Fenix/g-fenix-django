from django.db import models

class ContactInfo(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('tr', 'Türkçe'),
        ('es', 'Español'),
        ('bg', 'Български'),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    map_embed = models.TextField(help_text="Google Maps iframe embed kodu", blank=True, null=True)

    def __str__(self):
        return f"İletişim Bilgisi ({self.language})"


