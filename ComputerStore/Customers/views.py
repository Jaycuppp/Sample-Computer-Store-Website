from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

def Login_Auth(request):
    #Determines whether the User is logged in or not
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ("You have Logged in successfully!"))
            return redirect("HomePage")
        
        else:
            messages.success(request, ("There was a Login error. Try again."))
            return redirect("LoginPage")
        
    else:
        return render(request, "Login.html", {})
    
    
def User_Logout(request):
    logout(request)
    messages.success(request, ("You have logged out!"))
    return redirect("HomePage")


def User_Forgot_Password(request):
    return render(request, "User_Forgot_Password_Page.html")


def User_Register(request):
    if request.method == "POST":
        Form = UserRegistrationForm(request.POST)
        
        if Form.is_valid():
            Form.save()
            username = Form.cleaned_data["username"]
            password = Form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Account successfully Created!"))
            return redirect ("LoginPage")      
        
    else:
        Form = UserRegistrationForm()               

    return render(request, "User_Register.html", {
        'Form': Form,
        })