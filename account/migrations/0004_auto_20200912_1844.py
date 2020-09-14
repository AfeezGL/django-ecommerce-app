# Generated by Django 2.2 on 2020-09-12 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200802_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line_1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='Nigeria', max_length=250),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
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
        migrations.AddField(
            model_name='customer',
            name='postal_code',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('address_line_1', models.CharField(max_length=250, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(max_length=250, null=True)),
                ('state', models.CharField(max_length=250, null=True)),
                ('country', models.CharField(default='Nigeria', max_length=250)),
                ('postal_code', models.PositiveIntegerField(null=True)),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='DefaultAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryAddress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.DeliveryAddress')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Customer')),
            ],
        ),
    ]