# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
from django.db import models
from django.utils import timezone


class authors(models.Model):
    authorName = models.CharField(max_length=120)
    authorBio = models.CharField(max_length=1000)

class books(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=30)
    publisher = models.CharField(max_length=1000)
    coverImage = models.ImageField(upload_to='images/')
    authorInfo = models.ForeignKey(authors, on_delete=models.CASCADE)
    releasedDate = models.DateField(default=django.utils.timezone.now)
    def __str__(self):
        return self.name
