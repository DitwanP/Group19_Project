# Generated by Django 3.0.3 on 2020-03-06 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='stripe_id',
        ),
    ]
