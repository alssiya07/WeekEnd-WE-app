from django.urls import path
from weekendweb.views import RegisterView,LoginView,IndexView,add_cmd,sign_out_view,commeds_like_view

urlpatterns = [
    path('register/',RegisterView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('index/',IndexView.as_view(),name="home"),
    path("posts/<int:id>/commend/add",add_cmd,name="add-commend"),
    path("commend/<int:id>/like/add",commeds_like_view,name="add-likes"),

    path("logout",sign_out_view,name="signout"),


]