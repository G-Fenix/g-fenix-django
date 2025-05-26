from django.db import models

class BlogPost(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('tr', 'Türkçe'),
        ('es', 'Español'),
        ('bg', 'Български'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    content_preview = models.TextField(help_text="Blog yazısının kısa özeti veya giriş kısmı")
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', blank=True, null=True)
    published_at = models.DateField()

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return f"{self.title} ({self.language})"
