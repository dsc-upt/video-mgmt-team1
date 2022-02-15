from django.db import models
from .Category import Category
class Video (models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=500)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
