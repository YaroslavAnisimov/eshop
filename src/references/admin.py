from django.contrib import admin

# Register your models here.

from . import models 

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'Author_name',
        'Author_description',
        'created',
        'updated'
    ]

class ValueAdmin(admin.ModelAdmin):
    search_fields = ['author__Author_name']
    list_display = [
        'pk',
        'author',
        'Genre',
        'Reviews',
        'Rating'
    ]


admin.site.register(models.Value, ValueAdmin)

admin.site.register(models.Author, AuthorAdmin)

