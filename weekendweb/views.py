from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.

from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from django.contrib.auth.models import User
from weekendpost.models import Posts,Commends
from weekendweb.form import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from weekendweb.form import PostForm
from django import forms

# REGISTER
# -----------------------------------------------------------
class RegisterView(CreateView):
    template_name = "register.html"
    form_class=UserRegistrationForm
    success_url=reverse_lazy("login")

# Login
# -----------------------------------------------------------
class LoginView(FormView):
    template_name = "login.html"
    form_class=UserLoginForm

    def post(self,request,*arg,**kw):
        form=UserLoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,self.template_name,{"form":form})

# -----------------------------------------------------------
class IndexView(CreateView,ListView):
    template_name="index.html"
    form_class=PostForm
    success_url=reverse_lazy("home")
    model=Posts
    context_object_name="posts"

    def form_valid(self, form) :
        form.instance.posted_by=self.request.user     
        messages.success(self.request,"post uploaded")
        return super().form_valid(form)
    def get_queryset(self):
        return Posts.objects.exclude(posted_by=self.request.user).order_by("-posted_date")


def add_cmd(request,*args,**kw):
    id= kw.get("id")
    post=Posts.objects.get(id=id)
    cmd=request.POST.get("commend")
    Commends.objects.create(post=post,commend=cmd,commeded_by=request.user)
    messages.success(request,"Your commend is added")
    return redirect("home")

def commeds_like_view(request,*args,**kw):
    id=kw.get("id")
    cmd=Commends.objects.get(id=id)
    cmd.commeds_like.add(request.commeded_by)
    return redirect("home")

def sign_out_view(request,*args,**kw):
    logout(request)
    return redirect("login")