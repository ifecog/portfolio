# Generated by Django 4.1 on 2023-08-18 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0015_about_about_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='percentage',
        ),
    ]