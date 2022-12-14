from django.db import models
from django.forms import ModelForm
from datetime import datetime,date
from django.contrib.auth.models import AbstractUser,User
from django.conf import settings

# Create your models here.
# Create your models here.
class Categorie(models.Model):
    nom=models.CharField(max_length=30)
    image=models.ImageField()
    
    def __str__(self):
        return self.nom
    
#class todo model
class Todo(models.Model):
    titre=models.CharField(max_length=30)
    details=models.TextField()
    has_been_done=models.BooleanField(default=False)
    date_creation=models.DateTimeField(default = datetime.today())
    date_completion=models.DateTimeField(default = date.today())
    date_echeance=models.DateTimeField(default = datetime.today())
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.titre
    
class User(AbstractUser):
   pass
    