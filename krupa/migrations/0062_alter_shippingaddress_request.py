# Generated by Django 5.1 on 2024-11-26 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0061_alter_shippingaddress_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='krupa.request'),
        ),
    ]
