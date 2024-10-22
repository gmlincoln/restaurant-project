from django.db import models

# Create your models here.
class FoodModel(models.Model):
    
    food_image = models.ImageField(upload_to='Media/Food_Pic', null=True)
    food_name = models.CharField(max_length=200, null=True)
    food_ingredients = models.CharField(max_length=200, null=True)
    food_price= models.FloatField(null=True)

class EventModel(models.Model):

    event_image = models.ImageField(upload_to='Media/Event_Pic', null=True)
    event_name = models.CharField(max_length=100, null=True)
    event_price = models.FloatField(null=True)
    event_description = models.TextField(max_length=500, null=True)


class ChefModel(models.Model):

    chef_image = models.ImageField(upload_to='Media/Chef_Pic', null=True)
    chef_name = models.CharField(max_length=100, null=True)
    chef_type = models.CharField(max_length=70, null=True)
    chef_details= models.TextField(max_length=300)



class ReservedTableModel(models.Model):

    customer_name = models.CharField(max_length=100, null=True)
    email =  models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    booking_date = models.DateField(null=True)
    booking_time = models.TimeField(null=True)
    no_of_people = models.PositiveIntegerField(null=True)
    message = models.TextField(max_length=300, null=True)
