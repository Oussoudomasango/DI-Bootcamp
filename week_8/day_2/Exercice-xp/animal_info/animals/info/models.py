from django.db import models

# Create your models here.
class Families(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
    
class Person(models.Model):
    name = models.CharField(max_length=30)
    legs = models.IntegerField()
    weight = models.DecimalField(decimal_places=2,max_digits=1000)
    height = models.DecimalField(decimal_places=2,max_digits=1000)
    speed  = models.IntegerField()
    family = models.ForeignKey(Families,on_delete=models.CASCADE)