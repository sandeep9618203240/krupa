# Generated by Django 5.1 on 2024-11-26 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0066_alter_request_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]