from django.db import models
from ckeditor.fields import RichTextField
from birthday import BirthdayField, BirthdayManager

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    body = RichTextField()
    github_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    birthday = BirthdayField()

    objects = BirthdayManager()

    def __str__(self):
        return self.name

    class Mete:
        verbose_name = 'About'
        verbose_name_plural = 'About'
