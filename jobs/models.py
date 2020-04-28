from django.db import models
from django.urls import reverse
from django.utils import timezone

class AddJob(models.Model):
    jobName = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    minAge = models.PositiveIntegerField()
    maxAge = models.PositiveIntegerField()
    qualification = models.CharField(max_length=1000)
    vacancy = models.PositiveIntegerField()
    generalFee = models.PositiveIntegerField()
    obcFee = models.PositiveIntegerField()
    scstFee = models.PositiveIntegerField()
    payment = models.CharField(max_length=100,default=1)
    addedDate = models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)

    class Meta:
        ordering = ["-addedDate"]

    def __str__(self):
        return self.jobName

    def get_absolute_url(self):
        return reverse('jobs:viewJob', kwargs={"id": self.id})


class JobApply(models.Model):
    jobName = models.CharField(max_length=100)
    jobID = models.PositiveIntegerField()
    candidateFirstName = models.CharField(max_length=50)
    candidateMiddleName = models.CharField(max_length=50, blank=True)
    candidateLastName = models.CharField(max_length=50)
    relativeType = models.CharField(max_length=10,default='Father')
    fatherFirstName = models.CharField(max_length=50)
    fatherMiddleName = models.CharField(max_length=50, blank=True)
    fatherLastName = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    aadhaar = models.CharField(max_length=12)
    caste = models.CharField(max_length=20)
    addr1 = models.CharField(max_length=100)
    village1 = models.CharField(max_length=100)
    post1 = models.CharField(max_length=100)
    panchayat1 = models.CharField(max_length=100)
    ward1 = models.CharField(max_length=100)
    block1 = models.CharField(max_length=100)
    district1 = models.CharField(max_length=100)
    city1 = models.CharField(max_length=100)
    pin1 = models.PositiveIntegerField()
    addr2 = models.CharField(max_length=100)
    village2 = models.CharField(max_length=100)
    post2 = models.CharField(max_length=100)
    panchayat2 = models.CharField(max_length=100)
    ward2 = models.CharField(max_length=100)
    block2 = models.CharField(max_length=100)
    district2 = models.CharField(max_length=100)
    city2 = models.CharField(max_length=100)
    pin2 = models.PositiveIntegerField()
    qualification = models.CharField(max_length=50)

    board1 = models.CharField(max_length=200, default=None,blank=True)
    percentage1 = models.CharField(max_length=10,default=1,blank=True)
     
    board2 = models.CharField(max_length=200, default=None,blank=True)
    percentage2 = models.CharField(max_length=10,default=1,blank=True)
    
    board3 = models.CharField(max_length=200, default=None,blank=True)
    percentage3 = models.CharField(max_length=10,default=1,blank=True)

    pic = models.ImageField(upload_to='candidates/pics/')
    signhin = models.ImageField(upload_to='candidates/signhin/')
    signeng = models.ImageField(upload_to='candidates/signeng/')

    status = models.CharField(max_length=5, default='APPL')
    appliedDate = models.DateTimeField(auto_now=False, auto_now_add=False,default=timezone.now)

    payStatus = models.CharField(max_length=4, default='PEND')

    transactionID = models.CharField(max_length=200, default=0) 

    
    class Meta:
        ordering = ["-appliedDate"]

    def __str__(self):
        return self.email


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    jobid = models.CharField(max_length=10000)
    orderDate = models.DateTimeField(auto_now=False, auto_now_add=False,default=timezone.now)

    class Meta:
        ordering = ["-orderDate"]

    def __str__(self):
        return (self.email, ' JobID: ', self.jobid)