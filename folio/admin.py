from django.contrib import admin
from .models import About
from django.utils.html import format_html

# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'name', 'title')
    list_display_links = ('name', 'thumbnail', 'title')


admin.site.register(About, AboutAdmin)
