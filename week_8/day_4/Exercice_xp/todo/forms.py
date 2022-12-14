from django import forms
from .models import Todo,Categorie
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class TodoForm(forms.ModelForm):
    # Categorie=forms.CharField(label='categorie')
    
    class Meta:
        model=Todo
        fields=['titre','details','date_creation','date_echeance','categorie']
        # 'date_creation','date_completion','date_echeance']



class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # model= User
        fields = ('username', 'email', 'password1', 'password2')
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    