from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from products.models import books


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ebooks = models.ManyToManyField(books, blank=True)
	Email = models.CharField(max_length = 40)
	Username = models.CharField(max_length = 20)
	name = models.CharField(max_length = 40)
	Address = models.CharField(max_length = 40)
	phoneNumber = models.CharField(max_length = 10)
	nickName = models.CharField(max_length = 20)
	password = models.CharField(max_length = 40)
	def __str__(self):
		return self.user.username

class creditCards (models.Model):
	name = models.CharField(max_length = 40)
	card_number = models.CharField(max_length = 20)
	expDate = models.CharField(max_length = 5)
	cardType = models.CharField(max_length = 15)
	cvv = models.CharField(max_length = 3)
	Username = models.CharField(max_length = 20)
	
class shippingAddress (models.Model):
	address = models.CharField(max_length = 40)
	city = models.CharField(max_length = 20)
	state = models.CharField(max_length = 2)
	zipCode = models.CharField(max_length = 5)
	Username = models.CharField(max_length = 20)

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)