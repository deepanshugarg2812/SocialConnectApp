from django.db import models

class UserModel(models.Model):
    genderTypes = ( ('M', 'Male'),
        ('F', 'Female'))

    username = models.CharField(max_length=100,unique=True,null=False)
    firstName = models.CharField(max_length=100,null=False)
    lastName = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=False)
    gender = models.CharField(max_length=1,choices=genderTypes)
    age = models.IntegerField()

    def __str__(self):
        return self.username