# Generated by Django 4.2.2 on 2023-06-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalagro', '0010_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way')], default='Pending', max_length=50),
        ),
    ]
