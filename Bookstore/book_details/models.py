from django.db import models
from django.urls import reverse

from accounts.models import Profile
from products.models import books
# Create your models here.

class BookAuthor(models.Model):
    authorName = models.CharField(max_length=100)
    authorBio = models.CharField(max_length=1000)

    def __str__(self):
        return self.authorName


class BookInfo(models.Model):
    bookName = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=30)
    publisher = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    authorName = models.ForeignKey(BookAuthor, on_delete=models.CASCADE)
    coverImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.bookName

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookRatings(models.Model):
    bookRating = models.CharField(max_length=1000) #temporary
