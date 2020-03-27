from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DonateBlood(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author2 = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    dateofbirth = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=200)
    last_donation = models.CharField(max_length=200, blank=True, null=True)
    frequency = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)
    address = models.TextField()
    zip_code = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)


    @property
    def title(self):
        return self.name

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}: {}".format(self.name, self.email)


class BloodBanks(models.Model):
    blood_bank_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    about = models.CharField(max_length=200)


    def __str__(self):
        return "{} : {}".format(self.email, self.blood_bank_name)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return "{} : {}".format(self.name, self.message[:20])