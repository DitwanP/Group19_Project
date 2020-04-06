# Generated by Django 3.0.3 on 2020-04-06 00:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_books_releasedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='releaseDate',
        ),
        migrations.AddField(
            model_name='books',
            name='releasedDate',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 0, 56, 22, 426959, tzinfo=utc)),
        ),
    ]
