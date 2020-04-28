from django.urls import path, re_path

from . import views

app_name = 'jobs'

urlpatterns = [
    path('allJobs/', views.allJobs, name='allJobs'),
    re_path(r'(?P<id>\d+)/applyJob/$',views.applyJob, name='applyJob'),
    path('handleRequest/',views.handleRequest, name='handleRequest'),
    path('paymentStatus/',views.paymentStatus, name='paymentStatus'),
    path('reviewApplication/',views.reviewApplication, name='reviewApplication'),

]
