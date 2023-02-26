from django.db import models
from django.utils import timezone

class Contact(models.Model):
	full_name = models.CharField(max_length=30)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.full_name

