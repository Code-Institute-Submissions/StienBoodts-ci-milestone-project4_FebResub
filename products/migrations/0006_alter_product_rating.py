# Generated by Django 3.2.16 on 2023-01-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
    ]
