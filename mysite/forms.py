from django import forms

from .models import DonateBlood

class DonateBloodForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    dateofbirth = forms.CharField(max_length=200, required=False)
    weight = forms.CharField(max_length=200, required=False)
    blood_group = forms.CharField(max_length=200, required=False)
    last_donation = forms.CharField(max_length=200, required=False)
    frequency = forms.CharField(max_length=200, required=False)
    email = forms.CharField(max_length=200, required=False)
    mobile_no = forms.CharField(max_length=200, required=False)
    address = forms.CharField(max_length=10000, required=False)
    zip_code = forms.CharField(max_length=20, required=False)
    message = forms.CharField(max_length=10000, required=False)
    gender = forms.CharField(max_length=200, required=False)

class BloodBanksForms(forms.Form):
    blood_bank_name = forms.CharField(max_length=200)
    contact_person = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    about = forms.CharField(max_length=200)
