# Generated by Django 4.1.4 on 2022-12-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='photo',
            new_name='background_photo',
        ),
        migrations.AddField(
            model_name='about',
            name='display_photo',
            field=models.ImageField(default=1, upload_to='photos/%y/%m/%d/'),
            preserve_default=False,
        ),
    ]
