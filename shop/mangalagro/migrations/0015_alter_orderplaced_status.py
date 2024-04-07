# Generated by Django 4.2.2 on 2023-06-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalagro', '0014_rename_description_complaint_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('On The Way', 'On The Way')], default='Pending', max_length=50),
        ),
    ]