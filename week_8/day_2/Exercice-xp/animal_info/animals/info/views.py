
from django.shortcuts import render
from .models import Families,Person

def family(request,x):
    liste=[]
    for j in Person.objects.all():
        if j.family.id==x:
            liste.append(j)
    
    print(liste)
    context = {
        'animaux' : liste,
        'k': x
    }
    return render(request,'family.html',context)

def animals(request,x):
    liste=[]
    for j in Person.objects.all():
        if j.id==x:
            liste.append(j)
            break
    context = {
        'animaux' : liste,
        'id' : x
    }
    return render(request,'animal.html',context)