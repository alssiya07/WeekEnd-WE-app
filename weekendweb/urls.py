from django.urls import path
from weekendweb import views

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="signup"),
    path('login/',views.LoginView.as_view(),name="login"),
]