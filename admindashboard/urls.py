from django.urls import path, re_path

from django.contrib.auth.views import LogoutView


from . import views

app_name = 'admindashboard'

urlpatterns = [
    path('login/', views.userLogin, name='userLogin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    re_path(r'addReminder/$',views.addReminder,name='addReminder'),
    re_path(r'(?P<id>\d+)/deleteRem/$',views.deleteRem,name='deleteRem'),
    path('profile/', views.profile, name='profile'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('allCandidates/', views.allCandidates, name='allCandidates'),
    path('jobWiseCandidates/', views.jobWiseCandidates, name='jobWiseCandidates'),
    path('jobWiseSeleCandidates/', views.jobWiseSeleCandidates, name='jobWiseSeleCandidates'),
    path('addJob/', views.addJob, name='addJob'),
    path('editJob/', views.editJob, name='editJob'),
    path('allJobs/', views.allJobs, name='allJobs'),
    re_path(r'(?P<id>\d+)/editJob/$',views.editJob,name='editJob'),
    re_path(r'(?P<id>\d+)/deleteJob/$',views.deleteJob,name="deleteJob"),
    path('candidatesApplied/', views.viewCandDetails, name='viewCandDetails'),
    path('candidatesSelected/', views.viewSeleCandDetails, name='viewSeleCandDetails'),
    path('prepareNewMail/', views.sendNewMail, name='sendNewMail'),
    re_path(r'(?P<id>\d+)/printCand/$', views.printCand, name='printCand'),
    re_path(r'(?P<id>\d+)/prepareMail/$', views.prepareMail, name='prepareMail'),
    path('prepareNewMail/', views.prepareNewMail, name='prepareNewMail'),
    path('prepareMail/', views.sendMail, name='sendMail'),
    re_path(r'(?P<id>\d+)/deleteCandidate/$',views.deleteCandidate,name="deleteCandidate"),
    path('peopleQueries/', views.peopleQueries, name='peopleQueries'),
    re_path(r'(?P<id>\d+)/deleteQuery/$',views.deleteQuery,name="deleteQuery"),
    re_path(r'(?P<id>\d+)/prepareQueryMail/$', views.prepareQueryMail, name='prepareQueryMail'),
    path('prepareQueryMail/', views.sendQueryMail, name='sendQueryMail'),
]
