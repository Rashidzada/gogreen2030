from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
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
    return render(request,'register_view.html')

@login_required(login_url='login_view')
def profile(request):
    return render(request,'profile.html')


def about_view(request):
    return render(request,'about_view.html')