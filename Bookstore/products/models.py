# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class books(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    price = models.FloatField()
    image = models.ImageField(default='default.png')


    def __str__(self):
        return self.name

