# Generated by Django 2.2 on 2020-06-22 15:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200622_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='order_id'),
        ),
    ]
