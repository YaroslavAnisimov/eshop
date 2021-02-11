# Generated by Django 3.1.5 on 2021-02-05 12:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 5, 12, 22, 44, 523732, tzinfo=utc), verbose_name='Created date time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Created date time'),
        ),
    ]