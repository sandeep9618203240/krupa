# Generated by Django 5.1 on 2024-10-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0014_estimate_estimateitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='estimate_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='expiry_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
