# Generated by Django 5.1 on 2024-10-25 08:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0019_salesorder_salesorderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_received', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('bank_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_number', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('deposited_to', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_deducted', models.CharField(blank=True, default='yes', max_length=3, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=50, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('shipping_charges', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('adjustment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='krupa.request')),
            ],
        ),
    ]
