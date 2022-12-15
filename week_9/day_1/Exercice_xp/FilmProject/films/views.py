from django.shortcuts import render
from .forms import FilmForm,DirectorForm,PosteForm,DeleteFilmForm,CommentaireForn
from . import forms
from django.contrib import messages
from films.models import Categorie,Pays,Directeur,Film,Poste
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from . import models
from django.contrib import messages


# Create your views here.
def home(request):
    film=Film.objects.all()
    context={
        'film':film
    }
    return render(request,'homepage.html',context)
#........................................
def add_film(request):
    form= forms.FilmForm()
    if request.method== 'POST':
        form=forms.FilmForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.save()
            form=FilmForm()
            messages.success(request, 'Film ajoutez avec succes') # ignored
            return redirect('homepage')
    return render(request,'film/AddFilm.html',{'form':form})
#.................................
#Director form
def add_director(request):
    form= forms.DirectorForm()
    if request.method== 'POST':
        form=forms.DirectorForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.save()
            form=DirectorForm()
    return render(request,'directeur/AddDirector.html',{'form':form})
#.............................................................

