from django.contrib import admin

# Register your models here.
from references import models

class DictionariesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(models.Authors, DictionariesAdmin)
admin.site.register(models.Series, DictionariesAdmin)
admin.site.register(models.Genres, DictionariesAdmin)
admin.site.register(models.Publishers, DictionariesAdmin)
admin.site.register(models.AgeCategories, DictionariesAdmin)
# admin.site.register(models.BookFormats, DictionariesAdmin)




# from django.contrib import admin
# # Register your models here.
# from . import models 
# # registration of the model and class
# # the django admin site documentation

# class BookAdmin(admin.ModelAdmin):
#     #search_fields = ['book__book_name']
#     list_display = [
#         'pk',
#         'book_name',
#         'book_description',
#         'author',
#         'age',
#         'rating',
#         'created',
#         'updated']    

# class AuthorAdmin(admin.ModelAdmin):
#     search_fields = ['book__book_name']
#     list_display = [
#         'pk',
#         'book',
#         'author_name']    

# class GenreAdmin(admin.ModelAdmin):
#     list_display = [
#         'pk',
#         'book',
#         'genre_type']

# class AgeAdmin(models.ModelAdmin):
#     list_display = [
#         'pk',
#         'book',
#         'age_category']

# class PublishingAdmin(models.ModelAdmin):
#     list_display = [
#         'pk',
#         'book',
#         'publishing']


# admin.site.register(models.Book, BookAdmin)
# admin.site.register(models.Author, AuthorAdmin)
# admin.site.register(models.Genre, GenreAdmin)
# admin.site.register(models.Age, AgeAdmin)
# admin.site.register(models.Publishing, PublishingAdmin)



# class AuthorAdmin(admin.ModelAdmin):
#     list_display = [
#         'pk',
#         'name',
#         'description',
#         'created',
#         'updated'
#     ]

# class OpinionAdmin(admin.ModelAdmin):
#     search_fields = ['author__name']
#     list_display = [
#         'pk',
#         'author',
#         'Genre',
#         'Reviews',
#         'Rating'
#     ]
 
# admin.site.register(models.Author, AuthorAdmin)
# admin.site.register(models.Opinion, OpinionAdmin)


