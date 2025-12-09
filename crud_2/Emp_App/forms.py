from django import forms
from .models import Employee

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

dept_choices = [
    ('IT','IT'),
    ('ADMIN','ADMIN'),
    ('SALES','SALES'),
    ('ACCOUNT','ACCOUNT'),
    ('HR','HR'),
    ('FINANCE','FINANCE'),
    ('INSURANCE','INSURANCE')
]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'eid':'EMPLOYEE ID',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'age':'AGE',
            'gender':'GENDER',
            'city':'CITY',
            'mobile':'MOBILE',
            'address':'ADDRESS',
            'dept':'DEPARTMENT',
            'sal':'SALARY',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY'
        }
        widgets = {
            'eid':forms.NumberInput(attrs={
                'placeholder':'E.g.,101',
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name',
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'city':forms.TextInput(attrs={
                'placeholder':'E.g.,Mumbai',
            }),
            'mobile':forms.TextInput(attrs={
                'placeholder':'+91 ***** *****',
            }),
            'address':forms.Textarea(attrs={
                'placeholder':'E.g.,Maharashtra , Mumbai',
                'rows':'3',
            }),
            'dept':forms.Select(choices=dept_choices),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com',
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password',
            })
        }