from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    image = models.ImageField(default='media/default.png')
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    price = models.FloatField()

    def __str__(self):
        return self.name