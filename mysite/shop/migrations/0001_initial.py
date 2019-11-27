# Generated by Django 2.2.7 on 2019-11-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('description', models.TextField(default='')),
                ('seller', models.CharField(default='sahara', max_length=100)),
                ('product_pic', models.ImageField(default='item.png', upload_to='products')),
            ],
        ),
    ]
