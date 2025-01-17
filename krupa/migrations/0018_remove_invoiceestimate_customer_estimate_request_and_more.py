# Generated by Django 5.1 on 2024-10-23 06:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0017_alter_invoiceestimate_due_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceestimate',
            name='customer',
        ),
        migrations.AddField(
            model_name='estimate',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='krupa.request'),
        ),
        migrations.AddField(
            model_name='invoiceestimate',
            name='customer_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoiceestimate',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='krupa.request'),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='customer_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
