from django.db import models
from authapp.models import UserModel

class Friends(models.Model):
    user1 = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user1')
    user2 = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user2')
    areFriends = models.BooleanField(default=False)

class Post(models.Model):
    title = models.CharField(max_length=100,null=False)
    description = models.TextField(max_length=100,null=False)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    username = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Likes(models.Model):
    username = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return "liked by {} on post {}".format(self.username.username,self.post.title)

class Comment(models.Model):
    username = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,null=False)

    def __str__(self):
        return "Commented by {} on post {}".format(self.username.username,self.post.title)
