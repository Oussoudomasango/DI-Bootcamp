from django.shortcuts import render
from .models import Gif, Category
from .forms import GifForm,Category

# Create your views here.
def Homepage(request):
    context = {
        'page_title': "Homepage",
        'gifs': Gif.objects.all()
    }
    return render(request, 'homepage.html', context)

def Addnewgif(request):
    context = {
        'page_title' : "Add",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = GifForm(request.POST) # the Person Form
        # check if it's valid:',
        if form.is_valid():
            form.save()
            form_uploader_name = form.cleaned_data['uploader_name']
            form_title = form.cleaned_data['title']
            form_URL = form.cleaned_data['URL']
            form_category = form.cleaned_data['category']

            context['formInfo'] = {
                    'uploader_name' : form_uploader_name,
                    'title': form_title,
                    'URL': form_URL,
                    'category ': form_category
                }
            print(context['formInfo'])
            return render(request, 'add_new.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'add_new.html', context)

    else:
        # GET, generate blank form
        context['form'] = GifForm()
    return render(request, 'add_new.html', context)

def Addnewcategory(request):
    context = {
        'page_title' : "Add",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = Category(request.POST) # the Person Form
        # check if it's valid:',
        if form.is_valid():
            form.save()
            form_name = form.cleaned_data['name']

            context['formInfo'] = {
                    'name' : form_name,

                }
            print(context['formInfo'])
            return render(request, 'add_category.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'add_category.html', context)

    else:
        # GET, generate blank form
        context['form'] = Category()
    return render(request, 'add_category.html', context)   