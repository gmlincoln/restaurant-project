from django.shortcuts import render,redirect
from django.http import HttpResponse

from myApp.models import *



"""


USER END START


"""







def homePage(req):
    
    return render(req, 'user/index.html')

def aboutPage(req):
    
    return render(req, 'myAdmin/user/about.html')

def menuPage(req):
    
    foods = FoodModel.objects.all()
    
    return render(req, 'myAdmin/user/menu.html', {'foods':foods})

def eventsPage(req):

    events = EventModel.objects.all()
    
    return render(req, 'myAdmin/user/events.html', {'events': events})

def chefsPage(req):
    
    return render(req, 'myAdmin/user/chefs.html')

def contactPage(req):
    
    return render(req, 'myAdmin/user/contact.html')

def bookTable(req):
    
    return render(req, 'myAdmin/user/book-table.html')


"""


USER END FINISH


"""


"""


ADMIN PANEL START


"""

def dashboardPage(req):
    
    return render(req,'dadmin/index.html')


def addFood(req):
    
    if req.method == 'POST':
        food_image = req.FILES.get('fimage')
        food_name = req.POST.get('fname')
        food_ingredients = req.POST.get('fingredient')
        food_price = req.POST.get('fprice')
        
        foods = FoodModel(
            food_image = food_image,
            food_name = food_name,
            food_ingredients = food_ingredients,
            food_price = food_price
        )
        foods.save()
        return redirect('foodList')
    
    return render(req,'myAdmin/admin/add-food.html')

def foodList(req):
    
    foods = FoodModel.objects.all()
    
    return render(req,'myAdmin/admin/food-list.html', {'foods':foods})

def deleteFood(req,id):
    
    food = FoodModel.objects.filter(id=id)
    food.delete()
    
    return redirect('foodList')

def updateFood(req,id):
    
    food = FoodModel.objects.get(id=id)
    
    if req.method == 'POST':
        id = req.POST.get('id')
        
        food_data = FoodModel.objects.get(id=id)
        
        if req.FILES.get('fimage'):
            food_image = req.FILES.get('fimage')
        else:
            food_image = food_data.food_image
           
        food_name = req.POST.get('fname')
        food_ingredients = req.POST.get('fingredient')
        food_price = req.POST.get('fprice')
        
        foods = FoodModel(
            id = id,
            food_image = food_image,
            food_name = food_name,
            food_ingredients = food_ingredients,
            food_price = food_price
        )
        foods.save()
        return redirect('foodList')
    
    return render(req, 'myAdmin/admin/upload-food.html', {'food':food})



def addEvent(req):

    if req.method == 'POST':

        event_image = req.FILES.get('eimage')
        event_name = req.POST.get('ename')
        event_price = req.POST.get('eprice')
        event_description = req.POST.get('edescription')

        events = EventModel(
            event_image = event_image,
            event_name = event_name,
            event_price = event_price,
            event_description = event_description, 
        )

        events.save()
        return redirect('eventList')


    return render(req,'myAdmin/admin/add-events.html')

def eventList(req):

    events = EventModel.objects.all()

    return render(req, 'myAdmin/admin/event-list.html', {'events':events})

def deleteEvent(req,id):

    data = EventModel.objects.filter(id = id)
    data.delete()

    return redirect('eventList')


"""


ADMIN PANEL END


"""



def loginPage(req):

    return HttpResponse('LoginPage')

def registerPage(req):

    return HttpResponse('registerPage')