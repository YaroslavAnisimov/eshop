from django.db import models
from django.contrib.auth import models as auth_models
from cart import models as cart_models

# Create your models here.
class OrderStatuses(models.Model):
    status = models.CharField(
        verbose_name='Status',
        max_length=50
    )

    def __str__(self):
        return self.status


class CustomerOrder(models.Model):
    customer_cart = models.OneToOneField(
        cart_models.CustomerCart,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='Basket'
    )

    status = models.ForeignKey(
        'OrderStatuses',
        verbose_name='Status',
        on_delete=models.PROTECT
    )

    phone = models.CharField(
        verbose_name='Phone',
        max_length=80,
        blank=True,
        default=''
    )
    
    country = models.CharField(
        verbose_name='Country',
        max_length=80,
        blank=True,
        default=''
    )

    city = models.CharField(
        verbose_name='City',
        max_length=80,
        blank=True,
        default=''
    )

    post_index = models.CharField(
        verbose_name='Post-code',
        max_length=80,
        blank=True,
        default=''
    )

    address1 = models.CharField(
        verbose_name='Address',
        max_length=120,
        blank=True,
        default=''
    )

    # address2 = models.CharField(
    #     verbose_name='Адрес 2',
    #     max_length=120,
    #     blank=True,
    #     default=''
    # )

    comments = models.TextField(
        verbose_name='Comments',
        max_length=1000,
        blank=True,
        default=''
    )

    create_date = models.DateTimeField(
        verbose_name='Date of creation',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='Date of changing',
        auto_now=True
    )

    def __str__(self):
        return f'Order #{self.pk}'









# from django.db import models

# class Order(models.Model): #order has 1 basket (cart) and to 1 order only 1 order could be related
#     cart = models.OneToOneField(
#         "cart.Cart",
#         verbose_name="Cart",
#         on_delete=models.PROTECT)
    
#     address = models.TextField("Address") #where to delivery
#     # phone = models.TextField("Phone")
#     # status = models.TextField("Status")


#     def __str__(self):
#         return f"order ID{self.pk}"
    