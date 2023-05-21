from django.db import models
from users.models import Customer


class Product(models.Model):
    name = models.CharField('Name', max_length=50, default='')
    price = models.BigIntegerField('Price', default=0)
    quantity = models.BigIntegerField('Quantity', default=0)
    description = models.TextField('Description')

    def __str__(self):
        return self.name + "\n\n" + self.description


class Cart(models.Model):
    user = models.ManyToManyField(Customer)
    product = models.ManyToManyField(Product)
    quantity = models.BigIntegerField('Quantity', default=1)


class Order(models.Model):
    date = models.DateField('Delivery date')
    city = models.CharField('City', max_length=30, default='')


class OrderProduct(models.Model):
    order = models.ManyToManyField(Order)
    product = models.ManyToManyField(Product)
