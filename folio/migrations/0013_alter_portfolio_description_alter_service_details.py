# Generated by Django 4.1.4 on 2022-12-22 07:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0012_portfolio_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='details',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
