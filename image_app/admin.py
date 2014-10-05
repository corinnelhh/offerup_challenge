from django.contrib import admin
from image_app.models import Image


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('Duplicate', 'Hash')
    list_display = ('id', 'fileName', 'Duplicate', 'Hash')

admin.site.register(Image, ImageAdmin)
