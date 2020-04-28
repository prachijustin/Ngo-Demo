from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


#ADMIN PROFILE 
class AdminProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/admin/', blank=True)

    def __str__(self):
         return self.user.username



class AdminReminder(models.Model):
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
      
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.content