from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from django_resized import ResizedImageField




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25,blank=True)
    image = ResizedImageField(size=[200,200],quality=100,upload_to='profile_pics', force_format='WEBP')
    description = models.CharField(max_length=100, blank=True)
    bio_link = models.CharField(max_length=300,blank=True)
    follows = models.ManyToManyField(User,related_name="follows",blank=True)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"



REASON = [
    
    ('SPAM','SPAM'),
    ('INAPPROPRIATE','INAPPROPRIATE'),
    ('NEGATIVE','NEGATIVE'),
    ('ABUSIVE','ABUSIVE'),
    
]


class UserReport(models.Model):
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reported_user')
    reason = models.CharField(max_length=100,choices=REASON)
    reporting_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reporting_user')
    date_reported = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.reported_user.username