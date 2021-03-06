# Generated by Django 2.2 on 2020-06-22 14:30

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20200622_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=['customer__username', 'id']),
        ),
    ]
