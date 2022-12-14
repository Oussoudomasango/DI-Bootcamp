from django.contrib import admin
from .models import Person,Post,ImageProfile #import the Person model
from .models import Questions

class QuestionAdm(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
        ]

admin.site.register(Questions,QuestionAdm)
# Register your models here.
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(ImageProfile)