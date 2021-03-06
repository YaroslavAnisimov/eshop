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




class AuthorInCart(models.Model): #link to the things what clients buying
    cart = models.ForeignKey(
        Cart,
        verbose_name="Cart",
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        "references.Author",
        verbose_name="Author in cart",
        on_delete=models.PROTECT)

    quantity = models.IntegerField("Quantity", default=1)
    price = models.DecimalField(
        "Price", 
        max_digits=5,
        decimal_places=2)

def __str__(self):
        return f"AuthorInCart ID {self.pk} {self.author.name} quantity {self.quantity} price {self.price}"

 
    