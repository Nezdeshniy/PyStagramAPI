from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='categories')
