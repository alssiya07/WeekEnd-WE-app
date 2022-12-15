from django.db import models
from django.db.models import Count
# Create your models here.
from django.contrib.auth.models import User

class Posts(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True)
    description=models.CharField(max_length=500)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    posted_date=models.DateField(auto_now_add=True)

    @property
    def posts_cmdcount(self):         
        qs=self.commend_set.all().annotate(u_count=Count("commeds_like")).ordered_by("-u_count")
        return qs

    @property
    def posts_cmd(self):
        return self.commends_set.all()

    def __str__(self):
        return self.title

class Commends(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    commend=models.CharField(max_length=500)
    commeded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    commeded_date=models.DateField(auto_now_add=True)
    commeds_like=models.ManyToManyField(User,related_name="like")

    @property
    def likescount(self):
        return self.commeds_like.all().count()

    def __str__(self):
        return self.commend

