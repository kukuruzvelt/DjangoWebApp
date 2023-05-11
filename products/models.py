from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=50, default='')
    price = models.BigIntegerField('Price', default=0)
    quantity = models.BigIntegerField('Quantity', default=0)
    description = models.TextField('Description')

    def __str__(self):
        return self.name + "\n\n" + self.description


class Cart(models.Model):
    user_id = models.BigIntegerField('User ID', default=0)
    product_id = models.BigIntegerField('Product ID', default=0)
