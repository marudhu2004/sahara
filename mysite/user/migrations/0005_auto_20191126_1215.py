# Generated by Django 2.2.7 on 2019-11-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='First', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Last', max_length=50),
        ),
    ]
