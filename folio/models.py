from django.db import models
from ckeditor.fields import RichTextField
from birthday import BirthdayField, BirthdayManager

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=80)
    background_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    display_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    body = RichTextField()
    city = models.CharField(max_length=30, default=False)
    country = models.CharField(max_length=30, default=False)
    phone = models.CharField(max_length=16, default=False)
    email = models.EmailField(max_length=254, default=False)
    github_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    birthday = BirthdayField()

    objects = BirthdayManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Skill(models.Model):
    name = models.CharField(max_length=80)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Resume(models.Model):
    name = models.CharField(max_length=45)
    document = models.FileField(upload_to='documents')
    
    def __str__(self):
        return self.name