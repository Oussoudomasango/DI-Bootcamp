from django.shortcuts import render
from .models import Todo,Categorie
from datetime import datetime
from .forms import TodoForm 
from django.shortcuts import redirect
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.contrib import messages
from django.conf import settings
from . import models
from django.contrib.auth.decorators import login_required
from datetime import date, time, datetime
from dateutil import parser
from django.utils import dateparse
# Create your views here.

def home(request):
    categories=Categorie.objects.all()
    context={
        'categories':categories
    }
    return render(request,'base.html',context)

@login_required
def todocreate(request):
    form= forms.TodoForm()  
    if request.method == 'POST':
        form= forms.TodoForm(request.POST or None)  
        if form.is_valid():
            form= form.save(commit=False)
            form.user= request.user
            form.save()
            form= TodoForm()
    
    return render(request,'todo_view.html',{'form':form}) 

def display_todos(request):
    # todos=Todo.objects.filter(id=id)
    categories=Categorie.objects.all()

    todos=Todo.objects.all()

    # todos.has_been_done='True'
    # todos.save()
    context={
        'todos':todos
    }
    return render(request,'display_todos.html',{'todos':todos,'categories':categories})

def display_todos_List(request,id):

    todos=Todo.objects.filter(id=id)
    for todos in todos:
        todos.has_been_done='True'
        # today=  todos.date_completion
        todos.date_completion=dateparse.parse("One year ago")
        todos.save()

    context={
        'todos':todos
    }
    return redirect('display_todos')
#todo done
def todo_done(request,user_id):
    categories=Categorie.objects.all()
    # context={
    #     'categories':categories
    # }
    todos=Todo.objects.filter(user_id=user_id)
    context={
        'todos':todos
    }
    return render(request,'todo_done.html',{'todos':todos,'categories':categories})
# def todo_done(request):
#     categories=Categorie.objects.all()
#     # context={
#     #     'categories':categories
#     # }
#     todos=Todo.objects.all()
#     context={
#         'todos':todos
#     }
#     return render(request,'todo_done.html',{'todos':todos,'categories':categories})
#delete tache
def delete(request,id):
    todos=Todo.objects.get(id=id)
    todos.delete()
#categorie 
@login_required
def todos_categories(request,id):
    todos=Todo.objects.filter(categorie_id=id)
    context={
        'todos':todos
    }
    return render(request,'todos_categories.html',context)
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.add_message(request, messages.INFO, 'Nom d\'utilisateur ou mot de passe incorecte')
    return render(request, 'connection/login.html', context={'form': form})
#signup
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            # login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'connection/register.html', context={'form': form})    
#..............................
def logout_user(request):
    
    logout(request)
    return redirect('home')
#filtre
def delai_date(request):
    todos=Todo.objects.all()
    date_achevement=todos.date_completion