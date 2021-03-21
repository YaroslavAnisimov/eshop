from django.db import models

class Order(models.Model): #order has 1 basket (cart) and to 1 order only 1 order could be related
    cart = models.OneToOneField(
        "cart.Cart",
        verbose_name="Cart",
        on_delete=models.PROTECT)
    
    address = models.TextField("Address") #where to delivery
    # phone = models.TextField("Phone")
    # status = models.TextField("Status")


    def __str__(self):
        return f"order ID{self.pk}"
    