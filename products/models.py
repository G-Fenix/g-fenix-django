from django.db import models

class Product(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('tr', 'Türkçe'),
        ('es', 'Español'),
        ('bg', 'Български'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.language})"

