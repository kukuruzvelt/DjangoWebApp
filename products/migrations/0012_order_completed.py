# Generated by Django 4.2 on 2023-05-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Is Completed'),
        ),
    ]
