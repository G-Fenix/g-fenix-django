from django.db import models

class Service(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('tr', 'Türkçe'),
        ('es', 'Español'),
        ('bg', 'Български'),
    ]

    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('data', 'Data Analysis'),
        ('web', 'Web Development'),
        ('python', 'Python Development'),
        ('ai', 'Artificial Intelligence'),
        ('cases', 'User Cases'),
        ('training', 'Training'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.language} - {self.category})"

