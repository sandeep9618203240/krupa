# Generated by Django 5.1 on 2024-11-16 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0043_rename_satus_salesorder_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoiceestimate',
            old_name='due_date',
            new_name='expiry_date',
        ),
        migrations.RenameField(
            model_name='salesorder',
            old_name='expected_shipment_date',
            new_name='expiry_date',
        ),
    ]