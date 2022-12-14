from django.shortcuts import render
from .models import Person, Post,Category # import the models from polls/models.py
from .formulaires import ContactForm,PersonForm,PostForm


person = Person.objects.filter(first_name="Maria", 
                               last_name = "Fez").first() 
                    # get the first object because Person.objects.filter returns a QuerSet (ie. a list)


def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : person,
    }

    if request.method == 'POST':

        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if we get data
        print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_email = form.cleaned_data['email']
            form_comment = form.cleaned_data['comment']
            context['formInfo'] = {
                    'name' : form_name,
                    'email': form_email,
                    'comment': form_comment
                }
            context['btnFormHidden'] = True # To hide the button is the form is successfully submitted
            # print the values to make sure their are correct
            print(context['formInfo'])
            return render(request, 'posts/homepage.html', context)
        else:
             # print the errors, just in case
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'posts/homepage.html', context)

    else:
        # GET, generate blank form
        context['form'] = ContactForm()
    return render(request, 'posts/homepage.html', context)


def posts(request):
    context = {
        'page_title' : "Posts",
        'user' : person,
        'posts' : Post.objects.filter(
                        author__first_name=person.first_name,
                        author__last_name=person.last_name
        )  
    }
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            post_to_add = form.save(commit=False)
            for attr, value in post_to_add.__dict__.items():
                print(f'{attr} : {value}')
            
            return render(request,'posts/posts.html',context)
           
    else:
         # GET, generate blank form
        context['form'] = PostForm()
    return render(request, 'posts/posts.html', context)


def signup(request):
    context = {
        'page_title' : "SignUp",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = PersonForm(request.POST) # the Person Form
        # check if it's valid:
        if form.is_valid():
            
            person_to_add = form.save() 
            person_added = Person.objects.filter(
                first_name=form.cleaned_data['first_name'],         
                last_name=form.cleaned_data['last_name'])
            print(person_added)
            print(person_to_add)
            form_first_name = form.cleaned_data['first_name']
            form_last_name = form.cleaned_data['last_name']
            form_birth_date = form.cleaned_data['birth_date']
            form_has_pet = form.cleaned_data['has_pet']
            form_number_pet = form.cleaned_data['number_pet']
            context['formInfo'] = {
                    'first_name' : form_first_name,
                    'last_name': form_last_name,
                    'birth_date': form_birth_date,
                    'has_pet': form_has_pet,
                    'number_pet': form_number_pet 
                }
            print(context['formInfo'])
            return render(request, 'posts/signup.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'posts/signup.html', context)

    else:
        # GET, generate blank form
        context['form'] = PersonForm()
    return render(request, 'posts/signup.html', context)