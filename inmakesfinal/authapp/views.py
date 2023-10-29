from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['repassword']
        if password == password2:
            if User.objects.filter(username=username):
                messages.info(request,'This Username already exist')
                return redirect('authapp:signup')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('authapp:login')
        else:
            messages.info(request,'Password does not match')
            return redirect('authapp:signup')

    return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bankapp:newpage')
        else:
            messages.info(request,'Username not found or password incorrect')
            return redirect('authapp:login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('bankapp:home')