# Generated by Django 3.1.7 on 2021-03-06 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0006_author_pic'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='references.author', verbose_name='Author in cart')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Cart')),
            ],
        ),
    ]