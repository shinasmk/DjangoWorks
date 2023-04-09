from django.contrib import admin

# Register your models here.

from photos.models import Category,Photo
admin.site.register(Category)
admin.site.register(Photo)