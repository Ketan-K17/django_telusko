from django.shortcuts import render, redirect

# this is the user's model. You don't need to create it manually, just use this.
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                print("Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
                user.save()
                print("User created")
                return redirect('login')
        else:
            print("Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')