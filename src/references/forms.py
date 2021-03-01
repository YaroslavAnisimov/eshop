from django import forms
from django.db.models import fields
from . import models

class AuthorForm (forms.ModelForm):
    class Meta:
        model = models.Author 
        fields = ('__all__')
    #    fields = ('name', 'description' )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get ('name')

        if name == "Yaroslav":
            self.add_error('name', 'This name is forbidden')
        return cleaned_data
    
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

    

