# Generated by Django 3.0.3 on 2020-03-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('availability', models.TextField(max_length=25)),
                ('image', models.ImageField(upload_to='pictures')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
