from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def topics_listing(request):
    return render(request,'topics_listing.html')


def contact(request):
    return render(request,'contact.html')


def topics_detail(request):
    return render(request,'topics_detail.html')


@login_required(login_url='login_view')
def dashboard(request):
    return render(request,'dashboard.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request=request,message=f'Invalid credentials')
            return redirect('login_view')
    return render(request,'login_view.html')

def logout_view(request):
    logout(request)
    return redirect('index')
      

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_role = request.POST.get('user_role')
        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                messages.error(request=request,message=f'Email already exists')
            elif User.objects.filter(username = username).exists():
                messages.error(request=request,message=f"Username taken")
            else:
                user = User.objects.create_user(username=username,email=email, password=password,is_staff = True)
                UserProfile.objects.create(user = user , user_role = user_role)
                messages.success(request=request,message=f'Account created successfully')
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(user=user,request=request)
                    return redirect('dashboard')
        else:
            messages.error(request=request,message=f'Your passwod not match')
    return render(request,'register_view.html')

@login_required(login_url='login_view')
def profile(request):
    return render(request,'profile.html')


def about_view(request):
    return render(request,'about_view.html')