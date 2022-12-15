from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

        # styling model form in dictionary format
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }


# for updation and creation use modelform else normal form

class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))