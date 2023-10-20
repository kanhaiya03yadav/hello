from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("About",views.About,name='About'),
    path("games",views.games,name='games'),
    path("Contact",views.contact,name='contact'),
]
