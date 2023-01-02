from rest_framework import serializers
from django.contrib.auth.models import User
from weekendpost.models import Posts,Commends


# user serializer
class UserSerialiizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","email","username","password"]

# encryption of password
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# commends
class CommendsSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    post=serializers.CharField(read_only=True)
    commeded_by=serializers.CharField(read_only=True)
    commeded_date=serializers.CharField(read_only=True)
    commeds_like=serializers.CharField(read_only=True)
    likescount=serializers.IntegerField(read_only=True)

    class Meta:
        model=Commends
        fields=["id","post","commend","commeded_by","commeded_date","commeds_like","likescount"]
    
# exracting question
    def create(self,validated_data):
        pst=self.context.get("post")
        usr=self.context.get("commeded_by")
        return pst.commends_set.create(commeded_by=usr,**validated_data)

# each posts and their commends
class PostsSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    posted_by=serializers.CharField(read_only=True)
    posts_cmd=CommendsSerializer(read_only=True,many=tuple)
    post_likescount=serializers.IntegerField(read_only=True)

    class Meta:
        model=Posts
        fields=["id","title",
        "description","image",
        "posted_by","posted_date","posts_cmd","post_likescount"]