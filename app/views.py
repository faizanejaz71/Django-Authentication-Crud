from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='/login')

def home(request):
    return render(request, 'crud.html')



def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect ('/login/')
        else:
            login(request, user)
            return redirect ('/crud/')

    return render(request, 'login.html')



def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')


    # Create a new User object with the provided information
        user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        )
    

        user.set_password(password)
        user.save()


        messages.info(request, 'Account Created Successfully')
    
        return redirect('/register/')

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')