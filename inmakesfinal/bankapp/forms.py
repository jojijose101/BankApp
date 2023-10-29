from django import forms

from django.db import models
from django.forms import ModelForm

from .models import Branches,BankAccount
from .models import Districts


class FormRegisterF(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    AC_TYPE = [
        ('Savings Account','Saving Account'),
        ('Current Account','Current Account'),
        ('Salary Account','Salary Account')
    ]
    materials_provide = [
        ('Credit Card','Credit Card'),
        ('Debit Card','Debit Card'),
        ('Cheque Book','Cheque Book')
    ]
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect,label='Gender')
    phone_number = forms.CharField(label='Phone Number')
    mail_id = forms.EmailField(label='Email')
    address = forms.CharField(widget=forms.Textarea,label='Address')
    district = forms.ModelChoiceField(queryset= Districts.objects.all(),empty_label='Select District',label='District')
    branch = forms.ModelChoiceField(queryset= Branches.objects.all(),empty_label='Select Branch',label='Branch')
    account_type = forms.ChoiceField(choices=AC_TYPE,label='Account Type')
    materials_provide = forms.MultipleChoiceField(choices= materials_provide,widget=forms.CheckboxSelectMultiple,label='Materials Provide')

class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class FormRegister(FormRegisterF):
    class Meta:
        model = BankAccount
        fields = '__all__'
        widgets = {
            'DOB': XYZ_DateInput(format=["%Y-%m-%d"],)
            }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branches.objects.none()
        if 'district' in self.data:
            try:
                dis_id = int (self.data.get('district'))
                self.fields['branch'].queryset = Branches.objects.filter(dist_id=dis_id).all()
            except TypeError or ValueError:
                pass

