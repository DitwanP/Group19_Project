# Generated by Django 3.0.3 on 2020-04-11 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=100)),
                ('authorBio', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='BookRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookRating', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('genre', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coverImage', models.ImageField(upload_to='images/')),
                ('authorName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_details.BookAuthor')),
            ],
        ),
    ]
