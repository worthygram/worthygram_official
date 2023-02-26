# Third party imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from parler.models import TranslatableModel, TranslatedFields
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _
from  embed_video.fields  import  EmbedVideoField



class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,unique=True,max_length=111)
    content =  models.TextField()
    image = ResizedImageField(size=[400, 500], quality=100,upload_to='post_images', force_format='WEBP',blank=True)
    video = models.FileField(upload_to='post/video',default='',blank=True)
    audio = models.FileField(upload_to='post/audio',default='',blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes',blank=True)


    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


            
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})


        

REASON = [
    
    ('SPAM','SPAM'),
    ('INAPPROPRIATE','INAPPROPRIATE'),
    ('NEGATIVE','NEGATIVE'),
    ('ABUSIVE','ABUSIVE'),
    
]


class PostReport(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.CharField(max_length=150,choices=REASON)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_reported = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.post.title



class Story_Urls(TranslatableModel):
    translations = TranslatedFields(
        urls = models.URLField(max_length=200,null=True),
    )

    def __str__(self):
        return self.urls or ''


class Story(TranslatableModel):
    slug = models.SlugField(_("Slug"),null=True,unique=True,max_length=200)
    
    translations = TranslatedFields(
    title = models.CharField(max_length=100),
    content =  models.TextField(),
    youtube_story = EmbedVideoField(blank=True,unique=True),
    image =  ResizedImageField(size=[400, 500], quality=90,upload_to='story_images', force_format='WEBP',blank=True),
    video = models.FileField(upload_to='stories/video',default='',blank=True),
    audio = models.FileField(upload_to='stories/audio',default='',blank=True),
    date_posted = models.DateTimeField(default=timezone.now),
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
 
    )
   
    def get_absolute_url(self):
        return reverse('blog:story-detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title 


class Do_Exercise(TranslatableModel):
    slug = models.SlugField(_("Slug"),null=True,unique=True,max_length=111)
    translations = TranslatedFields(
    title = models.CharField(max_length=100),
    
    content =  models.TextField(),
    youtube_exercise = EmbedVideoField(blank=True,unique=True),
    image =  ResizedImageField(size=[400, 500], quality=90,upload_to='exercise_images', force_format='WEBP',blank=True),
    video = models.FileField(upload_to='exercise/video',default='',blank=True),
    audio = models.FileField(upload_to='exercise/audio',default='',blank=True),
    date_posted = models.DateTimeField(default=timezone.now),
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
 
    )
    
   
    def get_absolute_url(self):
        return reverse('blog:story-detail', kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.title 


    


class Certify(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default='',null=True,blank=True)
    certify = models.FileField(upload_to='certificates',blank=True)
    certify_all = models.FileField(upload_to='certificates_all',blank=True,null=True)

    def __str__(self):
        return self.title or ''




class Quotes(TranslatableModel):
    
    translations = TranslatedFields(
        quotes = models.CharField(max_length=400,null=True)
    )
    
   

    def __str__(self):
        return self.quotes or ''

class Exercise(TranslatableModel):
    
    translations = TranslatedFields(
        exercise = models.CharField(max_length=400,null=True)
    )
    
   

    def __str__(self):
        return self.exercise or ''


class Do(TranslatableModel):
    
    translations = TranslatedFields(
        do = models.CharField(max_length=400,null=True)
    )
    
   

    def __str__(self):
        return self.do or ''




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment



@receiver(pre_save,sender=Do_Exercise)
def sulg_generator(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title+" "+str(sender.objects.count()))

@receiver(pre_save,sender=Story)
def sulg_generator(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title+" "+str(sender.objects.count()))

@receiver(pre_save,sender=Post)
def sulg_generator(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title+" "+str(sender.objects.count()))