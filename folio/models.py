from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=80)
    display_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    about_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    body = RichTextField()
    city = models.CharField(max_length=30, default=False)
    country = models.CharField(max_length=30, default=False)
    phone = models.CharField(max_length=16, default=False)
    email = models.EmailField(max_length=254, default=False)
    github_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Skill(models.Model):
    name = models.CharField(max_length=80)
    upload_time = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=45)
    document = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    web_url = models.URLField(max_length=100)
    github_url = models.URLField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=60)
    details = RichTextField()
    upload_time = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name
