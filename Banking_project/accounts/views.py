from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
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

# @login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.save()
        return redirect('profile')
    return render(request,'edit_profile.html')



# @login_required
def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if not user.check_password(old_password):
            return messages.error(request, "Your Old password is not match with new password")
        elif new_password != confirm_password :
            return messages.error(request, "Your miss match")
        else:
            if request.method == 'POST':
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request,user)
                return messages.success(request,"Password changed")
            return redirect('profile')
    return render(request,"change_password.html")

@login_required
def logout_page(request):
    logout(request)
    return render(request,'login.html')

# @login_required
def profile(request):
    return render(request,'profile.html')