# Generated by Django 2.2 on 2020-05-31 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]