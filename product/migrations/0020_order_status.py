# Generated by Django 2.2 on 2020-07-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('PND', 'Pending Shipment'), ('TRA', 'In Transit'), ('DLV', 'Delivered')], max_length=3, null=True),
        ),
    ]
