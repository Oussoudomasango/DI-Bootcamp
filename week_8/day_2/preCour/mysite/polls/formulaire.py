from datetime import datetime
from django import forms
from .models import Person
def validate_name(name):
    if (name.isalpha() == False):
        print("Invalid name")
        raise forms.ValidationError(f'The name {name} is invalid')

class ContactForm(forms.Form):
    name = forms.CharField(required=False, min_length=3,
            validators=[validate_name],
            widget=forms.TextInput(
                attrs = {
                        'placeholder': 'write your name here'
                }
            ))
    email = forms.EmailField(
        label = "Your email", 
        help_text = 'Must contain at least 8 characters', 
        min_length = 8,
        widget = forms.EmailInput(
            attrs={
                'placeholder' : 'write your email here'
            })
        )
       
    comment = forms.CharField(widget = forms.Textarea(
        attrs={
            'placeholder': 'write your comment'
        }
    ))



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField()
    released_date = forms.DateField()
    author = forms.ModelChoiceField(queryset=Person.objects.all())