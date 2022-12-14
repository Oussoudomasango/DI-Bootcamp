from django.contrib import admin
from .models import GifModel,Category
# Register your models here.

admin.site.register(GifModel)
admin.site.register(Category)