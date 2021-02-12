from django.contrib import admin

# Register your models here.

from . import models 

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
        'created',
        'updated'
    ]

class OpinionAdmin(admin.ModelAdmin):
    search_fields = ['author__name']
    list_display = [
        'pk',
        'author',
        'Genre',
        'Reviews',
        'Rating'
    ]
 

admin.site.register(models.Author, AuthorAdmin)

admin.site.register(models.Opinion, OpinionAdmin)


