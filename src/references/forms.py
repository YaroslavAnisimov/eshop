from django import forms
from references import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Authors
        fields = ['name']
    

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genres
        fields = ['name']


class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = ['name']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publishers
        fields = ['name']


class AgeCategoriesForm(forms.ModelForm):
    class Meta:
        model = models.AgeCategories
        fields = ['name']


class BookFormatsForm(forms.ModelForm):
    class Meta:
        model = models.BookFormats
        fields = ['name']








# from django import forms
# from django.db.models import fields
# from . import models

# class BookForm (forms.ModelForm):
#     class Meta:
#         model = models.Book 
#         # fields = ('__all__')
#         fields = ('book_name', 'pic', 'book_description' )

# class SearchForm(forms.Form):
#     q = forms.CharField(label="Search:") #query(?)
#     field=forms.CharField(widget=forms.HiddenInput)
#     direction=forms.CharField(widget=forms.HiddenInput)



    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get ('name')

    #     if name == "Yaroslav":
    #         self.add_error('name', 'This name is forbidden')
    #     return cleaned_data
    
    #name = forms.CharField(
    #    max_length=50,
    #    required=True,
    #    label="Author's name",
    #    help_text="Input some name"
    #)
    
    #description = forms.CharField(
    #    label="Author's description",
    #    required=False,
    #    widget=forms.Textarea
    #)

    

