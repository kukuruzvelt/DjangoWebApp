# Generated by Django 4.2 on 2023-05-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_banned_user_login_user_money_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_banned',
        ),
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]