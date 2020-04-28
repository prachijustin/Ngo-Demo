from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from jobs.models import AddJob, JobApply
from datetime import date
from front.models import ContactMsg

# Create your views here.
def index(request):
    queryset = AddJob.objects.filter(endDate__gte=date.today(),startDate__lte=date.today())
    upcom = AddJob.objects.filter(startDate__gte=date.today())[:3]
    jobset = AddJob.objects.all()
    joblen = len(jobset)

    candset = JobApply.objects.filter(payStatus='DONE')
    candlen = len(candset)

    querset = ContactMsg.objects.all()
    querlen = len(querset)
    print(upcom)
    context = {
        "jobList": queryset,
        'upcom':upcom,
        'joblen': joblen,
        'candlen': candlen,
        'querlen':querlen
    }
    return render(request, 'index.html',context)

def about(request):
    jobset = AddJob.objects.all()
    joblen = len(jobset)

    candset = JobApply.objects.filter(payStatus='DONE')
    candlen = len(candset)

    querset = ContactMsg.objects.all()
    querlen = len(querset)
    context = {
        'joblen': joblen,
        'candlen': candlen,
        'querlen':querlen
    }
    return render(request,'about.html',context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('form_name')
        email = request.POST.get('form_email')
        sub = request.POST.get('form_subject')
        msg = request.POST.get('form_message')

        instance = ContactMsg()
        instance.name = name
        instance.email = email
        instance.sub = sub
        instance.msg = msg
        instance.save()

        context = {
            'code': 'SUCCESS'
        }
        print('yy')
        return render(request,'contact.html',context)
    else:
        print('nnnn')
        return render(request,'contact.html')

def currentjobs(request):
    queryset = AddJob.objects.filter(endDate__gte=date.today(),startDate__lte=date.today())
    context = {
        "jobList": queryset,
    }
    return render(request,'currentJobs.html',context)

def upcomingjobs(request):
    queryset = AddJob.objects.filter(startDate__gte=date.today())
    context = {
        "jobList": queryset,
    }
    return render(request,'upcomingJobs.html',context)

def viewJob(request,id=None):
    job = get_object_or_404(AddJob, id=id)
    context ={
        "job":job,
    }
    return render(request, 'viewJob.html',context)


def contactMsg(request):
    if request.method == "POST":
        name = request.POST.get('form_name')
        email = request.POST.get('form_email')
        sub = request.POST.get('form_subject')
        msg = request.POST.get('form_message')

        instance = ContactMsg()
        instance.name = name
        instance.email = email
        instance.sub = sub
        instance.msg = msg
        instance.save()

        context = {
            'code': 'SUCCESS'
        }
        print('efffffffffffffffff')
        return render(request,'contact.html',context)
    else:
        print('nnnnnnnnnnnnn')
        return render(request,'contact.html')