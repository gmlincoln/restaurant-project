# Generated by Django 5.0.7 on 2024-09-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_reservedtablemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservedtablemodel',
            old_name='user_name',
            new_name='customer_name',
        ),
    ]
