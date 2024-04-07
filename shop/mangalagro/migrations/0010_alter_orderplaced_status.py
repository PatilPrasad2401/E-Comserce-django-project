# Generated by Django 4.2.2 on 2023-06-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalagro', '0009_alter_orderplaced_status_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('On The Way', 'On The Way'), ('Accepted', 'Accepted')], default='Pending', max_length=50),
        ),
    ]
