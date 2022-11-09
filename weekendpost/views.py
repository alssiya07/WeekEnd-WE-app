from django.shortcuts import render

# Create your views here.
from weekendpost.serializer import UserSerialiizer,PostsSerializer,commendsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from weekendpost.models import Posts,Commends
from rest_framework import authentication,permissions
from rest_framework.decorators import action


