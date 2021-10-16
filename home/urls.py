from django.urls import path
from home.views import *
urlpatterns =[
    path('',indexPage,name='index'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('register/',Register,name='register'),
    path('welcome/', welcome, name='home'),
]