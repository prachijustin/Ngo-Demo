from django.urls import path,re_path

from django.contrib.auth.views import LogoutView


from . import views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.about, name='about'),
    path('contactus/', views.contact, name='contact'),
    path('currentJobs/', views.currentjobs, name='currentjobs'),
    path('upcomingJobs/', views.upcomingjobs, name='upcomingjobs'),
    re_path(r'(?P<id>\d+)/viewJob/$',views.viewJob, name='viewJob'),
    path('contactusok/', views.contactMsg, name='contactMsg'),

]
