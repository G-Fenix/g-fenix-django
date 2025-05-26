from django.db import models

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('tr', 'Türkçe'),
    ('es', 'Español'),
    ('bg', 'Български'),
]

class PageContent(models.Model):
    page_key = models.CharField(max_length=50, help_text="sayfa anahtarı: örnek -> aboutus, ourvision, ourmission")
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='page_images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('page_key', 'language')
        verbose_name = 'Sayfa İçeriği'
        verbose_name_plural = 'Sayfa İçerikleri'

    def __str__(self):
        return f"{self.page_key} ({self.language})"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)

    class Meta:
        verbose_name = 'Ekip Üyesi'
        verbose_name_plural = 'Ekip Üyeleri'

    def __str__(self):
        return f"{self.name} ({self.language})"

class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=100, help_text="FontAwesome sınıf adı örn: fa-brands fa-instagram")
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)

    class Meta:
        verbose_name = 'Sosyal Medya Bağlantısı'
        verbose_name_plural = 'Sosyal Medya Bağlantıları'

    def __str__(self):
        return f"{self.platform} ({self.language})"
