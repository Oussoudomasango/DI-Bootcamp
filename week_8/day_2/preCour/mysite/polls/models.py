from django.db import models #import the models package. This line is already existing as soon as we use 'startapp'
from datetime import datetime, date
#Must inherit from Django Model class
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def person_age(self):
        current_date = date.today()
        current_age = current_date.year-self.birth_date.year
        return f'{current_age}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    released_date = models.DateField(default = datetime.now())
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name='categories', blank=True)
# related_name is to retrieve the categories from a post

    def __str__(self):
        return f'Category {self.name}'
    
class Questions(models.Model):
    questions=models.CharField(max_length=50)
    date_published=models.DateField()
    
    
class ImageProfile (models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    image = models.URLField()

    def __str__(self):
        return f'ImageProfile of {self.person}'