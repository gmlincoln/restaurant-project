from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

    chefs = ChefModel.objects.all()
    
    return render(req, 'myAdmin/user/chefs.html', {'chefs':chefs})

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
@login_required
def dashboardPage(req):
    
    return render(req,'dadmin/index.html')

@login_required
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


@login_required
def foodList(req):
    
    foods = FoodModel.objects.all()
    
    return render(req,'myAdmin/admin/food-list.html', {'foods':foods})


@login_required
def deleteFood(req,id):
    
    food = FoodModel.objects.filter(id=id)
    food.delete()
    
    return redirect('foodList')

@login_required
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


@login_required
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


@login_required
def eventList(req):

    events = EventModel.objects.all()

    return render(req, 'myAdmin/admin/event-list.html', {'events':events})


@login_required
def deleteEvent(req,id):

    data = EventModel.objects.filter(id = id)
    data.delete()

    return redirect('eventList')


@login_required
def addChef(req):

    if req.method == 'POST':
        chef_image = req.FILES.get('cimage')
        chef_name = req.POST.get('cname')
        chef_type = req.POST.get('ctype')
        chef_details = req.POST.get('cdetails')

        chef = ChefModel(
            chef_image = chef_image,
            chef_name = chef_name,
            chef_type = chef_type,
            chef_details = chef_details 
        )
        chef.save()
        return redirect('chefList')

    return render(req, 'myAdmin/admin/add-chefs.html')


@login_required
def chefList(req):

    chefs = ChefModel.objects.all()

    return render(req,'myAdmin/admin/chef-list.html', {'chefs':chefs})


@login_required
def updateChef(req,id):
     
    chefs = ChefModel.objects.get(id=id)

    if req.method == 'POST':
        id = req.POST.get('id')

        data = ChefModel.objects.get(id=id)

        if req.FILES.get('cimage'):
            chef_image = req.FILES.get('cimage')
        else:
            chef_image = data.chef_image

        chef_name = req.POST.get('cname')

        chef_type = req.POST.get('ctype')
        chef_details = req.POST.get('cdetails')

        chef = ChefModel(
            id = id,
            chef_image = chef_image,
            chef_name = chef_name,
            chef_type = chef_type,
            chef_details = chef_details 
        )
        chef.save()
        return redirect('chefList')
     
    return render(req, 'myAdmin/admin/update-chef.html', {'chef':chefs})


@login_required
def deleteChef(req,id):

    data = ChefModel.objects.filter(id=id)

    data.delete()

    return redirect('chefList')


"""


ADMIN PANEL END


"""


def registerPage(req):

    if req.method == 'POST':
        firstname = req.POST.get('rfname')
        lastname = req.POST.get('rlname')
        username = req.POST.get('rusername')
        email = req.POST.get('remail')
        password = req.POST.get('password')
        confirm_password = req.POST.get('re-password')

        if password == confirm_password:
            user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            email = email, 
            username = username,
            password =  confirm_password
            )
            return redirect('loginPage')

        else:
            return HttpResponse('Both password should be same!!!')

    return render(req, 'common/admin/registerPage.html')

def loginPage(req):

    if req.method =='POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(
            username = username,
            password = password
        )
        if user:
            login(req,user)
            return redirect('dashboardPage')
        else:
            return HttpResponse('Username or Password Wrong!')


    return render(req, 'common/admin/loginPage.html')


def logoutPage(req):

    logout(req)

    return redirect('loginPage')