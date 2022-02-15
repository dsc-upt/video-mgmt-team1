from django.contrib import admin
from .models.category import Category
from .models.video import Video
# Register your models here.

admin.site.register(Category)
admin.site.register(Video)
