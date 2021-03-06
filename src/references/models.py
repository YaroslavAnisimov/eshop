from django.db import models
# Create your models here.


class Authors(models.Model):
    name = models.CharField(
        verbose_name='Author name',
        max_length=80,
        null=True,
        unique=True
    )

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(
        verbose_name='Book episode',
        max_length=80,
        null=True,
        unique=True
    )

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        verbose_name='Book genre',
        max_length=80,
        null=True,
        unique=True
    )

    def __str__(self):
        return self.name


class Publishers(models.Model):
    name = models.CharField(
        verbose_name='Publisher',
        max_length=80,
        null=True,
        unique=True
    )

    def __str__(self):
        return self.name


class AgeCategories(models.Model):
    name = models.CharField(
        verbose_name='Age category',
        max_length=80,
        null=True,
        unique=True
    )

    def __str__(self):
        return self.name


# class BookFormats(models.Model):
#     name = models.CharField(
#         verbose_name='Формат книги',
#         max_length=80,
#         null=True,
#         unique=True
#    )

#     def __str__(self):
#         return self.name








# from django.db import models

# Create your models here.

# class Author(models.Model) :
#     #ID
#     name = models.CharField(
#         verbose_name="Name",
#         max_length=50, 
#         null=False,
#         blank=False) 
        
#     pic = models.ImageField(
#         verbose_name="Picture",
#         upload_to = "uploads/")

#     description = models.TextField(
#         verbose_name="Book description",
#         null=True,
#         blank=True)
    
#     created = models.DateTimeField(
#         verbose_name='Created date time',
#         auto_now=False,
#         auto_now_add=True)

#     updated = models.DateTimeField(
#         verbose_name='Updated date time',
#         auto_now=True)

 
#     def __str__(self):
#         return self.name

# # class AuthorPic(models.Model):
# #     name = "Picture name)",
# #     pic = models.ImageField,
# #     author = models.ForeignKey(Author)


# class Opinion(models.Model):
    
#     author = models.ForeignKey(
#         'references.Author',
#         verbose_name = 'Author',
#         on_delete = models.PROTECT,
#         related_name = 'Opinions')

#     Genre = models.CharField(
#         verbose_name="Genre name",
#         max_length=50)
    
#     Reviews = models.TextField(
#         verbose_name="Reviews",
#         null=True,
#         blank=True,
#         max_length=200)

#     Rating = models.PositiveIntegerField(
#         verbose_name="Rating value",
#         null=True,
#         blank=True)
    
#     def __str__(self):
#         return f'{self.author} {self.Genre} {self.Reviews} {self.Rating}'


    # we can describe tables in our DB by this Class (class Book)
    # ORM development
    # id/pk - django make automatically - columns = properties
    # class + () = object ; book_name = column with certain features
    # model field reference documentation
    # field options documentation


#class Home(models.Model):
    


# class Book(models.Model): 
#     book_name = models.CharField(
#         max_length=30,
#         verbose_name="Book title",
#         null=False,
#         blank=False)

#     pic = models.ImageField(
#         verbose_name="Picture",
#         upload_to = "uploads/",
#         null=True,
#         blank=True)

#     book_description = models.TextField(
#         verbose_name="Book description",
#         null=True,
#         blank=True)

#     author = models.CharField(
#         max_length=30,
#         verbose_name="Author name",
#         null=False,
#         blank=False)

#     genre_type = models.CharField(  
#         max_length=30,
#         verbose_name="Genre")
        

#     age = models.CharField(
#         verbose_name="Age category",
#         max_length=30,
#         null=True,
#         blank=True)

#     publishing = models.CharField(
#         verbose_name="Publishing",
#         max_length=30,
#         null=True,
#         blank=True)


#     rating = models.PositiveIntegerField(
#         verbose_name="Rating value",
#         null=True,
#         blank=True)

#     created = models.DateTimeField(
#         verbose_name='Created',
#         auto_now=False, # time of the last edditing
#         auto_now_add=True)

#     updated = models.DateTimeField(
#         verbose_name='Updated',
#         auto_now=True)


#     # class BookPic(models.Model):
#     #     name = "Picture name)",
#     #     pic = models.ImageField,
#     #     book = models.ForeignKey(Book)

#     def __str__(self): # OOP method
#         return self.book_name


# class Author(models.Model):

#     book = models.ForeignKey( # lesson 13
#         'references.Book', # the link to another class - Book 
#         verbose_name = 'Book',
#         on_delete = models.PROTECT,
#         related_name = 'authors') 

#     author_name = models.CharField(  #street in lesson 13 (2:10)
#         verbose_name="Author name",
#         max_length=30)

#     def __str__(self):
#         return f'{self.book.book_name} {self.author_name}' 
 

# class Genre(models.Model):

#     book = models.ForeignKey( 
#         'references.Book',  
#         verbose_name = 'Book',
#         on_delete = models.PROTECT,
#         related_name = 'genres') 

#     genre_type = models.CharField(  
#         verbose_name="Genre",
#         max_length=30)

#     def __str__(self):
#         return f'{self.book.book_name} {self.genre_type}' 


# class Age(models.Model):

#     book = models.ForeignKey( 
#         'references.Book', 
#         verbose_name = 'Book',
#         on_delete = models.PROTECT,
#         related_name = 'ages')

#     age_category = models.TextField(
#         verbose_name="Age category",
#         null=True,
#         blank=True)

#     def __str__(self):
#         return f'{self.book.book_name} {self.age_category}' 


# class Publishing(models.Model):

#     book = models.ForeignKey( 
#         'references.Book', 
#         verbose_name = 'Book',
#         on_delete = models.PROTECT,
#         related_name = 'publishings')

#     publishing = models.TextField(
#         verbose_name="Publishing",
#         null=True,
#         blank=True)

#     def __str__(self):
#         return f'{self.book.book_name} {self.publishing}' 


