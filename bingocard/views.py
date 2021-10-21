from django.shortcuts import render
import random

from django.views.decorators.csrf import csrf_exempt

from testapp.models import *
app_name = 'card'
def showCard(request):
    count = Question.objects.all().count()
    l = []
    for i in range(1,count):
        quesid = Question.objects.all()[i].id
        l.append(quesid)
    random.shuffle(l)
    row1 = []
    for i in range(1,6):
        row1.append(l.pop(0))
    row2 = []
    for i in range(1, 6):
        row2.append(l.pop(0))
    row3 = []
    for i in range(1, 6):
        row3.append(l.pop(0))
    row4 = []
    for i in range(1, 6):
        row4.append(l.pop(0))
    row5 = []
    for i in range(1, 6):
        row5.append(l.pop(0))
    random.shuffle(row1)
    random.shuffle(row2)
    random.shuffle(row3)
    random.shuffle(row4)
    random.shuffle(row5)
    data = {}
    data['tabledata'] = [row1,row2,row3,row4,row5]
    return render(request,'bingocard/show-card.html',data)





