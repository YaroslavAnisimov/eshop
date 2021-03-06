from django.db import models
from django.contrib.auth import models as auth_models


# # Create your models here.
class ExtUserData(models.Model):
    user = models.OneToOneField(
        auth_models.User,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name='User'
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
        default='Belarus'
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

    def __str__(self):
        return f'{self.phone}, {self.address1}, {self.post_index},  {self.city}, {self.country}'

# def init_base_data():
#     # if groups.objects.get(name='Customers') not None:
#     obj = auth_models.Group.objects.get_or_create(name='Customers')
#     if not obj:
#         obj.save()
#     # if groups.objects.get(name='Managers') not None:
#     obj = auth_models.Group.objects.get_or_create(name='Managers')
#     if not obj:
#         obj.save()
# init_base_data()