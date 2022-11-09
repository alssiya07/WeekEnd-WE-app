from rest_framework import serializers
from django.contrib.auth.models import User
from weekendpost.models import Posts,Commends


# user serializer
class UserSerialiizer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["email","username","password"]

# encryption of password
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# posts
class PostsSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    posted_by=serializers.CharField(read_only=True)
    posted_date=serializers.CharField(read_only=True)
    class Meta:
        model=Posts
        fields=["id","title","description","image","posted_by","posted_date"]

# commends
class commendsSerializer(serializers.ModelSerializer):
    created_by=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    class Meta:
        model=Commends
        fields=["post","commend","commeded_by","commeded_date"]
    
# exracting question
    def create(self,validated_data):
        pst=self.context.get("post")
        usr=self.context.get("commeded_by")
        return pst.commend_set.create(commeded_by=usr,**validated_data)

# each posts and their commends
class PostsSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    posted_by=serializers.CharField(read_only=True)
    posts_cmds=commendsSerializer(read_only=True,many=True)
    class Meta:
        model=Posts
        fields=["id","title","description",
        "image","posted_by","posted_date",
        "posts_cmds"]