from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt
from home.forms import CreateUserForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
app_name = 'home'
login_required(login_url='home:login')
def welcome(request):
    res = render(request,'home/welcome.html')
    return res
@csrf_exempt
def indexPage(request):
    return render(request,'home/login.html')

def Login(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home:home')
            else:
                messages.info(request,'username OR password is incorrect')
                context ={}
                return render(request,'home/login.html',context)
@csrf_exempt
def Register(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('home:login')
        context ={'form':form}
        return render(request,'home/register.html',context)


login_required(login_url='home:login')
def Logout(request):
    logout(request)
    return redirect('home:login')
