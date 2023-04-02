from django.db import models

# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)