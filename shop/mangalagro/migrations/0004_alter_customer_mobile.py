# Generated by Django 4.2.2 on 2023-06-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalagro', '0003_rename_address_customer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(default=''),
        ),
    ]
