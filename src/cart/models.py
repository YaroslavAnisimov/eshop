from django.db import models
from django.contrib.auth import models as auth_models
from mainapp import models as main_models

# from django.db import models
# from django.contrib.auth import get_user_model
# User = get_user_model()

class CustomerCart(models.Model): #basket settings
    customer = models.ForeignKey(
        auth_models.User,
        # User, 
        on_delete=models.PROTECT, #if delete user - controversion
        verbose_name='Customer',
        related_name='customer_carts',
        blank = False,
        null=True
    )

    create_date=models.DateTimeField(
        verbose_name='Date of creation',
        auto_now=True
    )

    update_date = models.DateTimeField(
        verbose_name='Date of change',
        auto_now=True
    )

#threshold - doscounts - dinamic parameter

    # @property
    # def total_summ(self):
    #     all_books = self.books.all()
    #     total = 0
    #     for book in all_books:
    #         total += book.total_price
    #     return total

    @property
    def get_books_count(self):
        count = 0
        
        for book in self.books_in_cart.all():
            count += book.qty
        
        return count

    @property
    def get_total_price(self):
        total_price = 0
        
        for book in self.books_in_cart.all():
            total_price += book.get_total_price
        
        return total_price

    def __str__(self):
        return f"cart ID {self.pk}"



class BooksInCart(models.Model): #link to the things what clients buying
    customer_cart = models.ForeignKey(
        'CustomerCart',
        on_delete=models.PROTECT,
        verbose_name='Basket',
        related_name='books_in_cart',
        blank=False,
        null=True   
    )

    # cart = models.ForeignKey(
    #     Cart,
    #     verbose_name="Cart",
    #     related_name="books",
    #     on_delete=models.CASCADE)

    book_card = models.ForeignKey(
        main_models.BookCard,
        on_delete=models.PROTECT,
        verbose_name='Book',
        related_name='book_cards'
    )

    qty = models.IntegerField(
        verbose_name='Amount'
    )

    # book = models.ForeignKey(
    #     "references.Book",
    #     verbose_name="Book in cart",
    #     on_delete=models.PROTECT)

    # quantity = models.IntegerField("Quantity", default=1)

    # price = models.DecimalField(
    #     "Price", 
    #     max_digits=5,
    #     decimal_places=2)

    price = models.DecimalField(
        verbose_name='Cost',
        max_digits=5,
        decimal_places=2
    )

    create_date = models.DateTimeField(
        verbose_name='Date of creation',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='Date of changing',
        auto_now=True
    )
    
    @property
    def get_total_price(self):
        return self.qty * self.price

# @property
# def total_price(self):
#     return self.book.price * self.quantity

# def __str__(self):
#         return f"BookInCart ID {self.pk} {self.book.book_name} quantity {self.quantity} price {self.price}"

    def __str__(self):
        return f'{self.book_card}, {self.qty}, {self.price} USD'
    