from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from weekendpost.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","image","description"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "discription":forms.Textarea(attrs={"class":"form-control","rows":10}),
            "image":forms.FileInput(attrs={"class":"form-select"})
        }

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()