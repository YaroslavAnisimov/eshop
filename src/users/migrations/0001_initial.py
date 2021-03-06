# Generated by Django 3.1.7 on 2021-03-22 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUserData',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='User')),
                ('phone', models.CharField(blank=True, default='', max_length=80, verbose_name='Phone')),
                ('country', models.CharField(blank=True, default='Belarus', max_length=80, verbose_name='Country')),
                ('city', models.CharField(blank=True, default='', max_length=80, verbose_name='City')),
                ('post_index', models.CharField(blank=True, default='', max_length=80, verbose_name='Post-code')),
                ('address1', models.CharField(blank=True, default='', max_length=120, verbose_name='Address')),
            ],
        ),
    ]
