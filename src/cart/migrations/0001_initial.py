# Generated by Django 3.1.7 on 2021-03-22 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Date of creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of change')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_carts', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='BooksInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='Amount')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of changing')),
                ('book_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_cards', to='mainapp.bookcard', verbose_name='Book')),
                ('customer_cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books_in_cart', to='cart.customercart', verbose_name='Basket')),
            ],
        ),
    ]
