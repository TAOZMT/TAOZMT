from django.shortcuts import render, redirect
from . models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def register_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not CustomUser.objects.filter(username=username).exists():
            if password == confirm_password:
                user = CustomUser()
                user.first_name = firstname
                user.last_name = lastname
                user.phonenumber = phonenumber
                user.username = username
                user.password = password
                user.save()

                login(request, user)

                return redirect('homepage')
            else:
                return render (request, 'users/register.html')
        else:
            return render (request, 'users/register.html')
        
    return render (request, 'users/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            if next_url:
                return redirect (next_url)
            else:
                return redirect('homepage')
        else:
            message = f'Invalid username or password. Please try again'
            messages.success(request, message)
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')

def forgot_password_page(request):
    pass

def logout_page(request):
    logout(request)
    return redirect ('login_page')