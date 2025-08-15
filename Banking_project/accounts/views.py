from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        messages.success(request,"Regisration completed!!!")
        return redirect('login')
    return render(request,'register.html')



def login_page(request):
    if request.method == 'POST':
        user = authenticate(request,username = request.POST['username'],
                        password = request.POST['password'])
        if user:
            login(request, user)
            return redirect('profile')
    
    return render(request,'login.html')



def logout_page(request):
    logout(request)
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')