from django.shortcuts import render
from .forms import GifModelForm,CategoryModelForm
from .models import GifModel,Category


from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.views.generic import DetailView


def homepage(request):
    context={
        'title': "homepage",
        'gifs': GifModel.objects.all
    }
    return render(request,'gifs/homepage.html',context)


class AddGif(TemplateView):
    
    form = GifModelForm
    template_name = 'gifs/addNewGif.html'

    def post(self, request, *args, **kwargs):

        form = GifModelForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
           # return HttpResponseRedirect(reverse_lazy('gifs/homepage.html', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)    

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class AddCategory(TemplateView):
    form = CategoryModelForm
    template_name = 'gifs/addNewCategory.html'
    def post(self, request, *args, **kwargs):
    
        form = CategoryModelForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
           # return HttpResponseRedirect(reverse_lazy('gifs/homepage.html', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)    

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def categorys(request, id):
    context = {
        'id': id,
        'page_title' : "Category",
        'gifs': GifModel.objects.filter(id=id)
    }
    return render(request, 'gifs/category.html', context)