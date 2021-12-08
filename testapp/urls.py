from django.urls import path, re_path
from testapp.views import *
urlpatterns =[
    path('starttest/',startTest,name='start'),
    path('test/',testPaper,name='testPaper'),
    re_path('result/(?P<pk>\d+)/',result,name='result'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('viewQuestion/',viewQuestion,name='viewQuestion'),
    re_path('deleteQuestion/(?P<pk>\d+)/',deleteQuestion,name='deleteQuestion'),
    re_path('updateQuestion/(?P<pk>\d+)/',updateQuestion,name='updateQuestion'),
    path('LetsBingo/',LetsBingo,name='letsBingo'),
]