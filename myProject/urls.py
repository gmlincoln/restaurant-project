"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('aboutPage/', aboutPage, name='aboutPage'),
    path('menuPage/', menuPage, name='menuPage'),
    path('eventsPage/', eventsPage, name='eventsPage'),
    path('chefsPage/', chefsPage, name='chefsPage'),
    path('contactPage/', contactPage, name='contactPage'),
    path('bookTable/', bookTable, name='bookTable'),
    
    
    path('dashboardPage/', dashboardPage, name='dashboardPage'),
    path('addFood/', addFood, name='addFood'),
    path('foodList/', foodList, name='foodList'),
    path('deleteFood/<int:id>', deleteFood, name='deleteFood'),
    path('updateFood/<int:id>', updateFood, name='updateFood'),
    path('addEvent/', addEvent, name='addEvent'),
    path('eventList/', eventList, name='eventList'),
    path('deleteEvent/<int:id>', deleteEvent, name='deleteEvent'),
    
    
    
    
    
    path('loginPage/', loginPage, name='loginPage'),
    path('registerPage/', registerPage, name='registerPage'),
    
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
