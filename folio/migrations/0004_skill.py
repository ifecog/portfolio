# Generated by Django 4.1.4 on 2022-12-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0003_about_city_about_country_about_email_about_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('html', models.IntegerField()),
                ('css', models.IntegerField()),
                ('python', models.IntegerField()),
                ('javascript', models.IntegerField()),
                ('postgresql', models.IntegerField()),
                ('dtl', models.IntegerField()),
            ],
        ),
    ]
