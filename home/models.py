from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_detail(models.Model):
    name = models.CharField(max_length=150,default=None)
    phone = models.CharField(max_length=10,default=None)
    gender = models.CharField(max_length=50,default=None)
    dob = models.CharField(max_length=100,default=None)
    district = models.CharField(max_length=50,default=None,null=True)
    skill = models.CharField(max_length=200,default=None)
    experience = models.CharField(max_length=500,default=None)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_data',default=None)
    
    def __str__(self) -> str:
        return self.name
    
class Dashboard(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    title = models.CharField(max_length=100,default='User',null=True)

    def __str__(self) -> str:
        return f'{self.title} - Dashboard'
     