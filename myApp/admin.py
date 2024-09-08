from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(FoodModel)
admin.site.register(EventModel)
admin.site.register(ChefModel)
admin.site.register(ReservedTableModel)