from django.shortcuts import render, get_object_or_404
from jobs.models import JobApply, AddJob, Orders
from django.http import HttpResponse, HttpResponseRedirect

from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from jobs.checksum import generate_checksum, verify_checksum
import os
import requests
from django.conf import settings


MERCHANT_KEY = 'testkey'
MID = 'testmid'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def allJobs(request):
    queryset = AddJob.objects.all()
    length = len(queryset)
    print(length)
    context = {
        "object_list": queryset,
    }
    return render(request, 'allJobs.html',context)


def applyJob(request, id=None): 
    job = get_object_or_404(AddJob, id=id)
    jobname = job.jobName
    print(jobname)
    if request.method == 'POST':
        response = {}
        captcha_rs = request.POST.get('g-recaptcha-response')
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': captcha_rs,
            'remoteip': get_client_ip(request)
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        response["status"] = verify_rs.get("success", False)
        response['message'] = verify_rs.get('error-codes', None) or "Unspecified error."

        if verify_rs['success']:
            jobInstance = JobApply()
            jobInstance.jobName = jobname
            jobInstance.jobID = id
            jobInstance.candidateFirstName = request.POST.get('candidateFirstName')
            jobInstance.candidateMiddleName = request.POST.get('candidateMiddleName')
            jobInstance.candidateLastName = request.POST.get('candidateLastName')
            jobInstance.fatherFirstName = request.POST.get('fatherFirstName')
            jobInstance.fatherMiddleName = request.POST.get('fatherMiddleName')
            jobInstance.fatherLastName = request.POST.get('fatherLastName')
            jobInstance.relativeType = request.POST.get('relative')
            jobInstance.dob = request.POST.get('dob')
            jobInstance.gender = request.POST.get('gender')
            jobInstance.email = request.POST.get('email')
            jobInstance.phone = request.POST.get('phone')
            jobInstance.aadhaar = request.POST.get('aadhaar')
            jobInstance.caste = request.POST.get('caste')
            jobInstance.addr1 = request.POST.get('addr1')
            jobInstance.village1 = request.POST.get('village1')
            jobInstance.post1 = request.POST.get('post1')
            jobInstance.panchayat1 = request.POST.get('panchayat1')
            jobInstance.ward1 = request.POST.get('ward1')
            jobInstance.block1 = request.POST.get('block1')
            jobInstance.district1 = request.POST.get('district1')
            jobInstance.city1 = request.POST.get('city1')
            jobInstance.pin1 = request.POST.get('pin1')
            jobInstance.addr2 = request.POST.get('addr2')
            jobInstance.village2 = request.POST.get('village2')
            jobInstance.post2 = request.POST.get('post2')
            jobInstance.panchayat2 = request.POST.get('panchayat2')
            jobInstance.ward2 = request.POST.get('ward2')
            jobInstance.block2 = request.POST.get('block2')
            jobInstance.district2 = request.POST.get('district2')
            jobInstance.city2 = request.POST.get('city2')
            jobInstance.pin2 = request.POST.get('pin2')
            jobInstance.qualification = request.POST.get('qualification')
            jobInstance.board1 = request.POST.get('board1')
            jobInstance.percentage1 = request.POST.get('percentage1')
            jobInstance.board2 = request.POST.get('board2')
            jobInstance.percentage2 = request.POST.get('percentage2')
            jobInstance.board3 = request.POST.get('board3')
            jobInstance.percentage3 = request.POST.get('percentage3')
            caste = request.POST.get('caste')
            jobInstance.caste = caste
            if caste == 'General':
                amt = job.generalFee
            elif caste == 'OBC':
                amt = job.obcFee
            else:
                amt = job.scstFee
            
            name = request.POST.get('candidateFirstName') + ' ' + request.POST.get('candidateLastName')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            jobid = id
            if 'pic' in request.FILES:
                print('found it')
                jobInstance.pic = request.FILES['pic']
            if 'signhin' in request.FILES:
                print('found it')
                jobInstance.signhin = request.FILES['signhin']
            if 'signeng' in request.FILES:
                print('found it')
                jobInstance.signeng = request.FILES['signeng']
        
            jobInstance.save()
            context = {
                'jobInstance': jobInstance
            }
            print('yayyyy...........')

            #checkout code................
            order = Orders(amount=amt, name =name, email=email, phone=str(phone), jobid =str(jobid) )
            order.save()

            # Request paytm to transfer the amount to your account after payment by user
            param_dict = {
                    'MID': MID,
                    'ORDER_ID': str(order.order_id),
                    'TXN_AMOUNT': str(amt),
                    'CUST_ID': email,
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'DEFAULT',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'http://gmtrealtech.com/jobs/handleRequest/',
                
            }
            param_dict['CHECKSUMHASH'] = generate_checksum(param_dict, MERCHANT_KEY)
            print('------',param_dict['CHECKSUMHASH'])
            return render(request,'paytm.html', {'param_dict': param_dict})
        else:
            context={
                'code': 'NO',
                'msg': 'Recaptcha Authentication Failed!',
                'sitekey': settings.RECAPTCHA_SITE_KEY,
                "jobName":jobname,
                "id": id,
                "genFee": job.generalFee,
                "obcFee": job.obcFee,
                "scstFee": job.scstFee,
            }
            return render(request,'applyJob.html',context)     
    else:
        context ={
            'sitekey': settings.RECAPTCHA_SITE_KEY,
            "jobName":jobname,
            "id": id,
            "genFee": job.generalFee,
            "obcFee": job.obcFee,
            "scstFee": job.scstFee,
        }
        print('naaa....')
        return render(request,'applyJob.html',context)


def reviewApplication(request):
    return render(request,'review.html')



@csrf_exempt
def handleRequest(request):
    #paytm will send post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
            print(checksum)
        else:
            print('no checksum')
    try:
        verify = verify_checksum(response_dict, MERCHANT_KEY, checksum)
    
        if verify:
            if response_dict['RESPCODE'] == '01':
                orderid = response_dict['ORDERID']
                order = get_object_or_404(Orders, order_id=orderid)
                print('email: ', order.email)
                print('jobid:', order.jobid)
                try:
                    jobUser = get_object_or_404(JobApply, jobID=order.jobid, email= order.email)
                    print(jobUser.payStatus)
                    jobUser.payStatus = 'DONE'
                    jobUser.transactionID = response_dict['TXNID']
                    jobUser.save()
                    print(jobUser.payStatus)
                    print('order successful')
                except Exception as e:
                    print('/////',e)
                
            else:
                print('order was not successful because' + response_dict['RESPMSG'])
    except Exception as e:
        print(e)
    return render(request, 'paymentstatus.html', {'response': response_dict})

def paymentStatus(request):
    return render(request,'paymentStatus.html')