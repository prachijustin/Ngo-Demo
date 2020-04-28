from django.db import models

# Create your models here.
class ContactMsg(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    sub = models.CharField(max_length=50,blank=True)
    msg = models.CharField(max_length=500)
   
    
    def __str__(self):
         return (self.email, ' Subject: ', self.sub)