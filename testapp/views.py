from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from testapp.models import Question
from testapp.forms import *
from django.contrib import messages
app_name = 'test'
import random

def testPaper(request):
    count = Question.objects.all().count()
    s=random.randint(1,count)
    question = Question.objects.get(id=s)
    data = {'ques':question}
    return render(request,'testapp/test-paper.html',data)

@csrf_exempt
def result(request,pk):
    data={}
    if request.method=="POST":
        v=request.POST['option']
        q=Question.objects.get(id=pk)
        if v==q.answer:
            data['msg']="Congratulations, Your answer is correct"
        else:
            data['msg']="Sorry, your answer is not correct"
    return render(request,'testapp/result.html',data)

def deleteQuestion(request,pk):
    if request.method == 'POST':
        print('hello from view')
        Question.objects.filter(id=pk).delete()
    return redirect('test:viewQuestion')


def addQuestion(request):
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                messages.success(request,'Question added successfully')
                return redirect('test:addQuestion')
        context={'form':form}
        return render(request,'testapp/add-question.html',context)
    else:
        return redirect('home:home')

def viewQuestion(request):
    #if request.method == 'POST':
    questions = Question.objects.all()
    count = questions.count()
    data={'questions' : questions,'total':count}
    return render(request,'testapp/view-question.html',data)
    #else:
     #   return redirect('home:home')

def testpage(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'testapp/result.html',context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'testapp/test-paper.html',context)

"""    if 'user' not in request.session:
        return redirect('home:index')
        
        """



