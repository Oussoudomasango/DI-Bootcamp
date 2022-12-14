from django.db import models
from datetime import datetime, date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Category {self.name}'

class GifModel(models.Model):
    title=models.CharField(max_length=30)
    url=models.URLField()
    category= models.ManyToManyField(Category,related_name='categories',blank=True)
    create_at=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.title}'
