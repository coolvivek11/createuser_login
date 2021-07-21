from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'home.html')

def userlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have logged successfully")
            return redirect('home')
        else:
            return HttpResponse("Invalid Credential")

def signup(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request, "user created successfully")
        return redirect('home')

    else:
        return HttpResponse("sorry please try again")

def userlogout(request):
    logout(request)
    messages.success(request,"logged out successfully, please come again")
    return redirect('home')