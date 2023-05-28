from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.BigIntegerField('Money', default=0)

    def __str__(self):
        return f"{self.user.email} {self.user.first_name}"

