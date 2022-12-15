from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from weekendweb.form import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login
# Create your views here.


# REGISTER
class RegisterView(View):
    def get(self,request,*args,**kw):
        form=UserRegistrationForm()
        return render(request,"register.html",{"form":form})

    def post(self,request,*args,**kw):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signup")
        else:
            return render(request,"register.html",{"form":form})

# LOGIN
class LoginView(View):
    def get(self,request,*args,**kw):
        form=UserLoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*arg,**kw):
        form=UserLoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                print("invalid")
                return redirect("login")