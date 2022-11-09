from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Posts(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True)
    description=models.CharField(max_length=500)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    posted_date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="liked_by")

    @property
    def posts_cmd(self):         
        return self.cmd_set.all()

    def __str__(self):
        return self.title

class Commends(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    commend=models.CharField(max_length=500)
    commeded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    commeded_date=models.DateField(auto_now_add=True)
    commeds_like=models.ManyToManyField(User,related_name="like")

    def __str__(self):
        return self.cmd

