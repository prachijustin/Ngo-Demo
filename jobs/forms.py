from django import forms
from django.contrib.auth.models import User
from jobs.models import AddJob, JobApply

QUALIFICATION = [
    ('Graduated','Graduated'),
    ('12th', '12th'),
    ('10th', '10th'),
]
class AddJobForm(forms.ModelForm):
    class Meta():
        model = AddJob
        fields = ('jobName','startDate','endDate','minAge','maxAge','qualification','vacancy','generalFee','obcFee','scstFee','payment')
        widgets = {
            'jobName': forms.TextInput(attrs={'class':'form-control'}),
            'startDate': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'endDate': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'minAge': forms.NumberInput(attrs={'class':'form-control'}),
            'maxAge': forms.NumberInput(attrs={'class':'form-control'}),
            'qualification': forms.Select(choices=QUALIFICATION,attrs={'class':'form-control'}),
            'vacancy': forms.NumberInput(attrs={'class':'form-control'}),
            'generalFee': forms.NumberInput(attrs={'class':'form-control'}),
            'obcFee': forms.NumberInput(attrs={'class':'form-control'}),
            'scstFee': forms.NumberInput(attrs={'class':'form-control'}),
            'payment': forms.TextInput(attrs={'class':'form-control'}),
        }

RELATIVE = [
    ('Father','Father'),
    ('Husband','Husband'),
]
GENDER = [
    ('Male','Male'),
    ('Female', 'Female'),
    ('Others','Others'),
]

CASTE = [
    ('General','General'),
    ('OBC','OBC'),
    ('SC','SC'),
    ('ST','ST'),
]
class JobApplyForm(forms.ModelForm):
    class Meta():
        model = JobApply
        fields = [
            'jobName',
            'jobID',
            'candidateFirstName',
            'candidateMiddleName',
            'candidateLastName',
            'relativeType',
            'fatherFirstName',
            'fatherMiddleName',
            'fatherLastName',
            'dob',
            'gender',
            'email',
            'phone',
            'aadhaar',
            'caste',
            'addr1',
            'village1',
            'post1',
            'panchayat1',
            'ward1',
            'block1',
            'district1',
            'city1',
            'pin1',
            'addr2',
            'village2',
            'post2',
            'panchayat2',
            'ward2',
            'block2',
            'district2',
            'city2',
            'pin2',
            'qualification',
            'pic',
            'signhin',
            'signeng',
            'board1',
            'percentage1',
            'board2',
            'percentage2',
            'board3',
            'percentage3',
        ]
        widgets = {
            'jobName':forms.TextInput(attrs={'class':'form-control'}),
            'jobID':forms.TextInput(attrs={'class':'form-control'}),
            'candidateFirstName': forms.TextInput(attrs={'required': True,'class':'form-control'}),
            'candidateMiddleName': forms.TextInput(attrs={'class':'form-control'}),
            'candidateLastName': forms.TextInput(attrs={'class':'form-control'}),
            'relativeType' : forms.Select(choices=RELATIVE,attrs={'class':'form-control'}),
            'fatherFirstName': forms.TextInput(attrs={'class':'form-control'}),
            'fatherMiddleName': forms.TextInput(attrs={'class':'form-control'}),
            'fatherLastName': forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(choices=GENDER,attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'aadhaar': forms.TextInput(attrs={'class':'form-control'}),
            'caste': forms.Select(choices=CASTE,attrs={'class':'form-control'}),
            'addr1': forms.TextInput(attrs={'class':'form-control'}),
            'village1': forms.TextInput(attrs={'class':'form-control'}),
            'post1': forms.TextInput(attrs={'class':'form-control'}),
            'panchayat1': forms.TextInput(attrs={'class':'form-control'}),
            'ward1': forms.TextInput(attrs={'class':'form-control'}),
            'block1': forms.TextInput(attrs={'class':'form-control'}),
            'district1': forms.TextInput(attrs={'class':'form-control'}),
            'city1': forms.TextInput(attrs={'class':'form-control'}),
            'pin1': forms.TextInput(attrs={'class':'form-control'}),
            'addr2': forms.TextInput(attrs={'class':'form-control'}),
            'village2': forms.TextInput(attrs={'class':'form-control'}),
            'post2': forms.TextInput(attrs={'class':'form-control'}),
            'panchayat2': forms.TextInput(attrs={'class':'form-control'}),
            'ward2': forms.TextInput(attrs={'class':'form-control'}),
            'block2': forms.TextInput(attrs={'class':'form-control'}),
            'district2': forms.TextInput(attrs={'class':'form-control'}),
            'city2': forms.TextInput(attrs={'class':'form-control'}),
            'pin2': forms.TextInput(attrs={'class':'form-control'}),
            'qualification' : forms.Select(choices=QUALIFICATION,attrs={'class':'form-control'}),
           
            'board1': forms.TextInput(attrs={'class':'form-control'}),

            'board2': forms.TextInput(attrs={'class':'form-control'}),
        
            'board3': forms.TextInput(attrs={'class':'form-control'}),
          
        }