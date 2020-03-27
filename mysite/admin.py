from django.contrib import admin
from .models import DonateBlood, BloodBanks,Contact
# Register your models here.
admin.site.register(DonateBlood)
admin.site.register(BloodBanks)
admin.site.register(Contact)