# Generated by Django 4.2 on 2023-05-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Delivery date')),
                ('city', models.CharField(default='', max_length=30, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.BigIntegerField(default=0, verbose_name='Order ID')),
                ('product_id', models.BigIntegerField(default=0, verbose_name='Product ID')),
            ],
        ),
    ]
