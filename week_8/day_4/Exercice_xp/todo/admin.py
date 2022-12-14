from django.contrib import admin
from .models import Categorie,Todo
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display=('id','nom','image')
admin.site.register(Categorie,AdminCategorie)

class AdminTodo(admin.ModelAdmin):
    list_display=('id','titre','details','has_been_done','date_creation','date_completion','date_echeance','categorie')
admin.site.register(Todo,AdminTodo)    

class AdminUser(admin.ModelAdmin):
    list_display=('id','username','first_name','last_name','email','password','is_staff','is_active','date_joined')
admin.site.register(User,AdminUser)
