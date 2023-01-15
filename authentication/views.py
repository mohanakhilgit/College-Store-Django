from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        re_password = request.POST['re_password']

        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Already Taken")
                return redirect('authentication:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email Already In Use")
                return redirect('authentication:register')
            else:
                new_user = User.objects.create_user(username, email, password)
                new_user.save()
                messages.success(request, "Your account has been successfully created.")

                return redirect('authentication:signin')
                
        else:
            messages.error(request, "Passwords don't match!")
            return redirect('authentication:register')

    return render(request, 'authentication/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('order:order_home', username)
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('authentication:signin')

    return render(request, 'authentication/login.html')


def sign_out(request):
    logout(request)
    return redirect('website:home')
