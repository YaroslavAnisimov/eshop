from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model): #basket settings
    customer = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, #if delete user - controversion
        blank = False,
        null=True
    )

    def __str__(self):
        return f"cart ID {self.pk}"



class BookInCart(models.Model): #link to the things what clients buying
    cart = models.ForeignKey(
        Cart,
        verbose_name="Cart",
        related_name="books",
        on_delete=models.CASCADE)
    book = models.ForeignKey(
        "references.Book",
        verbose_name="Book in cart",
        on_delete=models.PROTECT)

    quantity = models.IntegerField("Quantity", default=1)
    price = models.DecimalField(
        "Price", 
        max_digits=5,
        decimal_places=2)

def __str__(self):
        return f"BookInCart ID {self.pk} {self.book.book_name} quantity {self.quantity} price {self.price}"

 
    