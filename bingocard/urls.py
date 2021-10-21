from django.urls import path, re_path
from testapp.views import *
from bingocard.views import *
urlpatterns =[
    path('',showCard,name='showcard'),
]