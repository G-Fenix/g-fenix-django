from django.db import models


class Project(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('tr', 'Türkçe'),
        ('es', 'Español'),
        ('bg', 'Български'),
    ]

    CATEGORY_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('future', 'Future'),
        ('client', 'Client'),
        ('general', 'General'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.language} - {self.category})"

