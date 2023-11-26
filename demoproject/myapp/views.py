from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')

    return render(request,'login.html')

def newfun(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already exist')
                return redirect('/next')
            else:
                 user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                 user.save();
                 messages.info(request,"Sign-up successfully")
                 return redirect('/next/login')
        else:
            messages.info(request,"password doesn't match")
    return render(request,'home.html')

