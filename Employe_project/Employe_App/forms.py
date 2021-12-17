from django import forms
from django.forms import widgets
from django.forms.widgets import Input, NumberInput,TextInput,EmailInput

from .models import Employee

class DateInput(forms.DateInput):
    input_type = 'date'

class Employee_form(forms.ModelForm):
    class Meta:
        model= Employee
        fields = ['emp_id','emp_name','emp_mobile_no','emp_email','emp_address','pos','emp_dob','emp_pic']
        labels = {
            'emp_id':'Employee ID',
            'emp_name':'Employee Name',
            'emp_mobile_no': 'Employee Mobile no',
            'emp_email':'Employee Email ID',
            'emp_address':'Employee Address',
            'emp_dob':'Employee Date of birth',
            'pos':'Employee Postion',
            'emp_pic':'Employee Picture'

        }
        widgets = {
            'emp_id' : NumberInput(attrs = {
                'placeholder':'Enter ID'
            }),
            'emp_name' : TextInput(attrs = {
                'placeholder':'Enter Name'
            }),
            'emp_mobile_no' : NumberInput(attrs = {
                'placeholder':'Enter mobile No'
            }),
            'emp_address' : TextInput(attrs = {
                'placeholder':'Enter Employee Address'
            }),
            'emp_email' : EmailInput(attrs = {
                'placeholder':'Enter Email ID'
            }),
            'emp_dob': DateInput(),
        }


    def __init__(self,*args,**kwargs):
        super(Employee_form,self).__init__(*args,**kwargs)
        self.fields['pos'].empty_label = 'Select'
        self.fields['emp_mobile_no'].required = False



