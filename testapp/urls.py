from django.urls import path, re_path
from testapp.views import *
urlpatterns =[
    #path('',testpage,name='testpage'),
    path('test/',testPaper,name='test'),
    re_path('result/(?P<pk>\d+)/',result,name='result'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('viewQuestion/',viewQuestion,name='viewQuestion'),
    re_path('deleteQuestion/(?P<pk>\d+)/',deleteQuestion,name='deleteQuestion'),
]