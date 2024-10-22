# Generated by Django 5.0.7 on 2024-09-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_image', models.ImageField(null=True, upload_to='Media/Food_Pic')),
                ('food_name', models.CharField(max_length=200, null=True)),
                ('food_ingredients', models.CharField(max_length=200, null=True)),
                ('food_price', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
