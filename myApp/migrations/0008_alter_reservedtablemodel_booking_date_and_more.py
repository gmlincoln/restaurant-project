# Generated by Django 5.0.7 on 2024-09-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_reservedtablemodel_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservedtablemodel',
            name='booking_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservedtablemodel',
            name='booking_time',
            field=models.TimeField(null=True),
        ),
    ]
