from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	wallet_address = models.CharField(default="none",max_length=10)
	wallet_key = models.CharField(default="none",max_length=10)
	
	status = models.BooleanField(default=False)
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username



