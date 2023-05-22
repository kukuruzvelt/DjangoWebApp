from django.db import models
from users.models import Customer


class Product(models.Model):
    name = models.CharField('Name', max_length=50, default='')
    price = models.BigIntegerField('Price', default=0)
    quantity = models.BigIntegerField('Quantity', default=0)
    description = models.TextField('Description')

    def __str__(self):
        return f"{self.name} ( {self.description} ) - {self.price} : {self.quantity} left"


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    quantity = models.BigIntegerField('Quantity', default=1)

    def __str__(self):
        return f"{self.product.name} : {self.product.price} x {self.quantity} = {self.product.price * self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    date = models.DateField('Delivery date')
    city = models.CharField('City', max_length=30, default='')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
