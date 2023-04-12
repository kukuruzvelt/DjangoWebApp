from django.db import models


class User(models.Model):
    login = models.CharField('Login', max_length=50, default='')
    password = models.CharField('Password', max_length=20, default='')
    money = models.BigIntegerField('Money', default=0)
    is_banned = models.BooleanField('Is Banned', default=False)
    name = models.CharField('Name', max_length=20, default='')
