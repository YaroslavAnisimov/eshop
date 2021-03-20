from django import forms
from django.db.models import fields
from . import models

class BookForm (forms.ModelForm):
    class Meta:
        model = models.Book 
        # fields = ('__all__')
        fields = ('book_name', 'pic', 'book_description' )

class SearchForm(forms.Form):
    query = forms.CharField(label="Search:")
    field=forms.CharField(widget=forms.HiddenInput)
    direction=forms.CharField(widget=forms.HiddenInput)




    

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

    

