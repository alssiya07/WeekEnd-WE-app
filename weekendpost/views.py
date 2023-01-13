from django.shortcuts import render

# Create your views here.
from weekendpost.serializer import UserSerialiizer,PostsSerializer,CommendsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from weekendpost.models import Posts,Commends
from rest_framework import authentication,permissions
from rest_framework.decorators import action

# localhost:8000/users/

class UsersView(ModelViewSet):
    serializer_class=UserSerialiizer
    queryset=User.objects.all()

# ----------------------------------------------------------------------------------
# localhost:8000/posts/     post
# localhost:8000/posts/     get

class PostsView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PostsSerializer
    queryset=Posts.objects.all()

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

# -----------------------------------------------------------------------
    @action(methods=["GET"],detail=True)
    def posts(self,request,*args,**kwargs):  # courses provided
        qs=Posts.objects.values_list("post",flat=True)
        return Response(data=qs)



# ---------------------------------------------------------------------------------
# localhost:8000/posts/5/posts_likes/
    @action(methods=["GET"],detail=True)
    def posts_likes(self,request,*args,**kwargs):
        pst=self.get_object()       
        usr=request.user
        qs=pst.post_like.add(usr)
        return Response(data=qs)
# --------------------------------------------------------------------------------
# localhost:8000/posts/1/add_cmd/

    @action(methods=["POST"],detail=True)
    def add_cmd(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Posts.objects.get(id=id)
        usr=request.user
        serializer=CommendsSerializer(data=request.data,context={"commeded_by":usr,"post":pst})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# ----------------------------------------------------------------------------------
# localhost:8000/posts/1/list_cmds/

    @action(methods=["GET"],detail=True)
    def list_cmds(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Posts.objects.get(id=id)
        qs=pst.commends_set.all()
        serializer=CommendsSerializer(qs,many=True)
        return Response(data=serializer.data)


# ---------------------------------------------------------------------------------
# localhost:8000/posts/my_posts/
# class UserProfileViewSet(ModelViewSet):
#     queryset = UserProfile.objects.all()
#     authentication_classes = [authentication.TokenAuthentication]
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
    @action(methods=['GET'],detail=False)
    def my_posts(self,request,*args,**kwargs):
        qs=request.user.posts_set.all()
        serializer=PostsSerializer(qs,many=True)
        return Response(data=serializer.data)

# ----------------------------------------------------------------------------------
# localhost:8000/commends/1/cmd_likes/

class CommendsView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CommendsSerializer
    queryset=Commends.objects.all()
    

    @action(methods=["GET"],detail=True)
    def cmd_likes(self,request,*args,**kwargs):
        cmd=self.get_object()       
        usr=request.user
        qs=cmd.commeds_like.add(usr)
        return Response(data=qs)
