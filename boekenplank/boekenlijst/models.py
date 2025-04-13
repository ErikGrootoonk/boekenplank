from django.db import models

# Create your models here

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    language = models.CharField(max_length=8)
    cover_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
