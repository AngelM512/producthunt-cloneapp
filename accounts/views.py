from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def sign(request):
    if request.method == 'POST':
        # User has info and wants an account!

        if request.POST['password1'] == request.POST['password2']:   
            try: 
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/sign.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],
                password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')

    else:
        return render(request, 'accounts/sign.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO route to homepage 
    return render(request, 'accounts/logout.html')
