# Generated by Django 5.1 on 2024-10-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0020_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]