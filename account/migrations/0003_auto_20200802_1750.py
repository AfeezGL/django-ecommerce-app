# Generated by Django 2.2 on 2020-08-02 17:50

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20200622_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='')),
                ('address', models.TextField(null=True)),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='__str__')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
