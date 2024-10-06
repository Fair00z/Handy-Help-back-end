from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Worker_Detail(models.Model):
    name = models.CharField(max_length=150,default=None)
    phone = models.CharField(max_length=10,default=None)
    gender = models.CharField(max_length=50,default=None)
    dob = models.CharField(max_length=100,default=None)
    district = models.CharField(max_length=50,default=None,null=True)
    skill = models.CharField(max_length=200,default=None)
    experience = models.CharField(max_length=500,default=None)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_data',default=None)
    profile_img = models.ImageField(upload_to='profiles',default='profiles/default_profile.jpeg')
    
    def __str__(self) -> str:
        return self.name

class Client_Detail(models.Model):
    name = models.CharField(max_length=150,default=None)
    phone = models.CharField(max_length=10,default=None)
    gender = models.CharField(max_length=50,default=None)
    dob = models.CharField(max_length=100,default=None)
    district = models.CharField(max_length=50,default=None,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='client_data',default=None)
    profile_img = models.ImageField(upload_to='profiles',default='profiles/default_profile.jpeg')
    
    def __str__(self) -> str:
        return self.name
    
class Worker_Dashboard(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    title = models.CharField(max_length=100,default='User',null=True)

    def __str__(self) -> str:
        return f'{self.title} - Dashboard'

class Client_Dashboard(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    title = models.CharField(max_length=100,default='User',null=True)

    def __str__(self) -> str:
        return f'{self.title} - Dashboard'
    
class Worker(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    
    def __str__(self):
        return self.user.user_data.name  # type: ignore
class Client(models.Model):
    user = models.OneToOneField(User,models.CASCADE)

    def __str__(self):
        return self.user.username  # type: ignore
class Comment(models.Model):
    worker = models.ForeignKey(Worker,models.CASCADE)
    client = models.ForeignKey(Client,models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"{self.worker.user.user_data.name}'s review" # type: ignore
class Job_post(models.Model):
    work_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    work_location = models.CharField(max_length=300)
    description = models.TextField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    work_img = models.ImageField(upload_to='job_image/',null=True)
    thumbnail = models.ImageField(upload_to='job_image/thumbnail',null=True)

    def __str__(self):
        return self.work_name
    