# Generated by Django 5.1 on 2024-08-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gstin',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
