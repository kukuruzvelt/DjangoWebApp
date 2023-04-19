from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=50, default='')
    price = models.BigIntegerField('Price', default=0)
    quantity = models.BigIntegerField('Quantity', default=0)
    description = models.TextField('Description')
