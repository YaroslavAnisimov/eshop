from django.db import models

# Create your models here.

class Author(models.Model) :
    #ID
    name = models.CharField(
        verbose_name="Name",
        max_length=50, 
        null=False,
        blank=False) 
        
    pic = models.ImageField(
        verbose_name="Picture",
        upload_to = "uploads/")

    description = models.TextField(
        verbose_name="Book description",
        null=True,
        blank=True)
    
    created = models.DateTimeField(
        verbose_name='Created date time',
        auto_now=False,
        auto_now_add=True)

    updated = models.DateTimeField(
        verbose_name='Updated date time',
        auto_now=True)

 
    def __str__(self):
        return self.name

# class AuthorPic(models.Model):
#     name = "Picture name)",
#     pic = models.ImageField,
#     author = models.ForeignKey(Author)


class Opinion(models.Model):
    
    author = models.ForeignKey(
        'references.Author',
        verbose_name = 'Author',
        on_delete = models.PROTECT,
        related_name = 'Opinions')

    Genre = models.CharField(
        verbose_name="Genre name",
        max_length=50)
    
    Reviews = models.TextField(
        verbose_name="Reviews",
        null=True,
        blank=True,
        max_length=200)

    Rating = models.PositiveIntegerField(
        verbose_name="Rating value",
        null=True,
        blank=True)
    
    def __str__(self):
        return f'{self.author} {self.Genre} {self.Reviews} {self.Rating}'
    



