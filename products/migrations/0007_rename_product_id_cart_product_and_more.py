# Generated by Django 4.2 on 2023-05-21 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_cart_product_id_remove_cart_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='product_id',
            new_name='product',
        ),
    ]
