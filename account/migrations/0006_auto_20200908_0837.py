# Generated by Django 2.2 on 2020-09-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200908_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address_line_1',
            field=models.CharField(max_length=250, null=True),
        ),
    ]