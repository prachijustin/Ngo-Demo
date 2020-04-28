from django import forms
from django.contrib.auth.models import User
from admin_dashboard.models import AdminProfile


#admin profile form for User
class AdminProfileForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password','first_name','last_name')