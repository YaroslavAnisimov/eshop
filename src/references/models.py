from django.db import models

# Create your models here.

class Author(models.Model) :
    #ID
    Author_name = models.CharField(
        verbose_name="Name",
        max_length=50,
        null=False,
        blank=False
        ) 
    Author_description = models.TextField(
        verbose_name="Book description",
        null=True,
        blank=True
    )
 

