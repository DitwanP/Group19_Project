# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class books(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    authorBio = models.CharField(max_length=1000, default='place holder')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=30)
    publisher = models.CharField(max_length=1000)
    coverImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

