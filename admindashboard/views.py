from django.shortcuts import render, redirect
from django.contrib.auth.models import User

#imports for login & logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from jobs.models import JobApply, AddJob
from django.shortcuts import render, get_object_or_404, redirect

from jobs.forms import AddJobForm
from django.contrib import messages
from admindashboard.models import AdminReminder
from admindashboard.sendEmail import sendMailTo
from front.models import ContactMsg

# Create your views here.
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/gmtadmin/dashboard")
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            context={"msg":"Invalid Username or Password. Please try again!"}
            print(context)
            return render(request, 'login.html',context) 
    else:
        return render(request, 'login.html')
    

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        current_user = request.user.username
        candList = JobApply.objects.filter(payStatus='DONE')
        candSel = JobApply.objects.filter(status='SELE', payStatus='DONE')
        jobLen = AddJob.objects.all()
        reminders = AdminReminder.objects.all()
        query = ContactMsg.objects.all()
        context = {
                'username': current_user,
                'candLen': len(candList),
                'mailid': request.user.email,
                'jobLen': len(jobLen),
                'candSel': len(candSel),
                'reminder_list': reminders,
                'quer': len(query)
            }
        return render(request,'dashboard.html',context)
    
def addReminder(request):
    remInstance = AdminReminder()
    if request.method == 'POST':
        content = request.POST.get('content')
        remInstance.content = content
        remInstance.save()
        print('added....')
        return HttpResponseRedirect('/gmtadmin/dashboard/')
    return render(request,'dashboard.html')


def deleteRem(request, id=None):
    instance = get_object_or_404(AdminReminder, id=id)
    instance.delete()
    return HttpResponseRedirect('/gmtadmin/dashboard/')


def profile(request):
    return render(request, 'profile.html')

@login_required
def changePassword(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        #print('-------------', pass1)
        if pass1 == pass2:
            u = User.objects.get(username=request.user.username)
            u.set_password(pass1)
            u.save()
            print('--------yayayyy')
            update_session_auth_hash(request, u)
            return HttpResponseRedirect('/gmtadmin/dashboard/')
        else:
            print('------na')
            return HttpResponseRedirect('/gmtadmin/profile/')
      
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'profiles.html',{'form':form})


def allCandidates(request):
    queryuser = JobApply.objects.filter(payStatus='DONE')
    context = {
        'queryuser': queryuser
    }
    return render(request, 'allCandidates.html', context)


def addJob(request):
    registered = False
    if request.method == 'POST':
        print('---ok')
        job_form = AddJobForm(data=request.POST)
   
        if job_form.is_valid():
            instance = job_form.save(commit=False)
            instance.save()
            registered = True
            print('----yayyy')
            context = {
                'code':'SUCCESS',
                'msg': 'Job Added Successfully!'
            }
            return render(request,'addJob.html',context)
        else:
            print('nnaaa')
            print(job_form.errors)
    else:
        print('aaaaa')
        job_form = AddJobForm()
       

    return render(request,'addJob.html',
                        {'job_form':job_form,
                        'registered':registered})



def editJob(request, id=None):
    print("hello")
    job = get_object_or_404(AddJob, id=id)
   
    if request.method == 'POST':
        job_form = AddJobForm(request.POST or None, instance=job)
        try:
            if job_form.is_valid():
                job_form.save()
                print('--updated............')
                return HttpResponseRedirect("/gmtadmin/dashboard")
            else:
                print(job_form.errors)
        except Exception as e:
            messages.warning(request,"Job didn't saved. {}".format(e))
    
    else:
        job_form = AddJobForm(instance=job)
        print('------------got')
        context = {
            "job": job,
            "job_form": job_form,
        }
    return render(request, 'addJob.html', context)



def allJobs(request):
    queryset = AddJob.objects.all()
    length = len(queryset)
    print(length)
    context = {
        "jobList": queryset,
    }
    return render(request, 'adminAllJobs.html', context)


def deleteJob(request, id=None):
    instance = get_object_or_404(AddJob, id=id)
    instance.delete()
    context = {
                'code':'SUCCESS',
                'msg': 'Job Deleted Successfully!'
            }
    messages.success(request, "Job Deleted Successfully!")
    return HttpResponseRedirect('/gmtadmin/allJobs')



def jobWiseCandidates(request):
    jobList = AddJob.objects.all()
    candidateList = JobApply.objects.filter(payStatus='DONE')
    context = {
        'jobList': jobList,
        'candidateList': candidateList
    }
    return render(request,'jobWiseCandidates.html',context)

def viewCandDetails(request): 
    if request.method == 'POST':
        jobID = request.POST['nameOfJob']
        jobID = int(jobID)
        cand = JobApply.objects.filter(jobID = jobID, payStatus='DONE')
        jobList = AddJob.objects.all()
        context = {
            'jobList': jobList,
            'cand': cand
        }
        return render(request,'jobWiseCandidates.html', context)
    else:
        print('naaaaaaaa')
    return HttpResponseRedirect('/gmtadmin/jobWiseCandidates/')


def printCand(request, id=None):
    p = get_object_or_404(JobApply, id=id, payStatus='DONE')
    context = {
        'p':p
    }
    print('prinnn')
    return render(request,'printCandidate.html',context)

def prepareMail(request, id=None):
    p = get_object_or_404(JobApply,id=id, payStatus='DONE')
    context = {
        'mailid': p.email,
        'fname': p.candidateFirstName,
        'jobName': p.jobName,
        'jobID': p.jobID,
        'candid': p.pk
    }
    return render(request,'prepareMail.html', context)


def sendNewMail(request):
    if request.method == 'POST':
        tomail = request.POST['tomail']
        subject = request.POST['subject']
        msg = request.POST['msg']
        
        res = sendMailTo(tomail, subject, msg)
        if res == 'SUCCESS':
            
            context = {
                'code': 'SUCCESS',
                're': 'Mail sent successfully!'
            }
            return render(request,'prepareNewMail.html',context)
        else:
            context = {
                'code': 'FAIL',
                're': res
            }
      
            return render(request,'prepareNewMail.html',context)
    return render(request,'prepareNewMail.html')



def prepareNewMail(request):
    return render(request,'prepareNewMail.html')


def sendMail(request):
    if request.method == 'POST':
        tomail = request.POST['tomail']
        subject = request.POST['subject']
        msg = request.POST['msg']
        candid = request.POST['candid']
        res = sendMailTo(tomail, subject, msg)
        if res == 'SUCCESS':
            query_user = get_object_or_404(JobApply, id=candid,payStatus='DONE')
            query_user.status = 'SELE'
            query_user.save()
            context = {
                'code': 'SUCCESS',
                're': 'Mail sent successfully!'
            }
            return render(request,'prepareMail.html',context)
        else:
            context = {
                'code': 'FAIL',
                're': res
            }
      
            return render(request,'prepareMail.html',context)
    else:  
        render(request,'prepareMail.html')

def jobWiseSeleCandidates(request):
    jobList = AddJob.objects.all()
    candidateList = JobApply.objects.filter(status='SELE',payStatus='DONE')
    context = {
        'jobList': jobList,
        'candidateList': candidateList
    }
    return render(request,'jobWiseSeleCandidates.html',context)


def viewSeleCandDetails(request): 
    if request.method == 'POST':
        jobID = request.POST['nameOfJob']
        jobID = int(jobID)
        cand = JobApply.objects.filter(jobID = jobID, status='SELE',payStatus='DONE')
        jobList = AddJob.objects.all()
        context = {
            'jobList': jobList,
            'cand': cand
        }
        return render(request,'jobWiseSeleCandidates.html', context)
    else:
        print('naaaaaaaa')
    return HttpResponseRedirect('/gmtadmin/jobWiseSeleCandidates/')


def deleteCandidate(request,id=None):
    instance = get_object_or_404(JobApply, id=id,payStatus='DONE')
    instance.delete()
    context = {
                'code':'SUCCESS',
                'msg': 'Candidate Deleted Successfully!'
            }
    messages.success(request, "Candidate Deleted Successfully!")
    return HttpResponseRedirect('/gmtadmin/jobWiseCandidates/')

def peopleQueries(request):
    queryuser = ContactMsg.objects.all()
    context = {
        'queryuser': queryuser
    }
    return render(request,'peopleQueries.html',context)

def deleteQuery(request,id=None):
    instance = get_object_or_404(ContactMsg, id=id)
    instance.delete()
    context = {
                'code':'SUCCESS',
                'msg': 'Query Deleted Successfully!'
            }
    messages.success(request, "Query Deleted Successfully!")
    return HttpResponseRedirect('/gmtadmin/peopleQueries')


def prepareQueryMail(request, id=None):
    p = get_object_or_404(ContactMsg,id=id)
    context = {
        'mailid': p.email,
        'name': p.name,
        'sub': p.sub,
        'queryid': p.pk
    }
    return render(request,'prepareQueryMail.html', context)

def sendQueryMail(request):
    if request.method == 'POST':
        tomail = request.POST['tomail']
        subject = request.POST['subject']
        msg = request.POST['msg']
        queryid = request.POST['queryid']
        res = sendMailTo(tomail, subject, msg)
        if res == 'SUCCESS':
            query_user = get_object_or_404(ContactMsg, id=queryid)
            query_user.save()
            context = {
                'code': 'SUCCESS',
                're': 'Mail sent successfully!'
            }
            return render(request,'prepareQueryMail.html',context)
        else:
            context = {
                'code': 'FAIL',
                're': res
            }
      
            return render(request,'prepareQueryMail.html',context)
    else:  
        render(request,'prepareQueryMail.html')