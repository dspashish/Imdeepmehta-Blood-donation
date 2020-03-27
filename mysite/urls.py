
from django.urls import path
from django.views.generic import TemplateView

from .views import (
 homepage,
login,
logout,
register,
creatorlogin,
donor_detail,
blood_list,
blood_detail,
blood_detail_ABP,
blood_update,
blood_detail_user,
blood_detail_ABN,
blood_detail_AN,
blood_detail_AP,
blood_detail_BN,
blood_detail_BP,
blood_detail_ON,
blood_detail_OP,
BloodBankCreateView,
blood_bank_list,
blood_bank_detail,
contact
)
urlpatterns = [
    path('', homepage, name='home'),
    path('choice/', TemplateView.as_view(template_name="choice.html"), name="choice"),
    path('login/', login, name='login'),
    path('logout/', logout, name="logout"),
    path('register/', register, name="register"),
    path('creator/', creatorlogin, name="creator"),
    path("donor_details/", donor_detail, name="donor_detail"),
    path("donor_list/", blood_list, name='donor_list'),
    path("donor_list/<int:pk>/", blood_detail),
    path("donor_ABP/", blood_detail_ABP),
    path("donor_list/<int:pk>/edit/", blood_update, name="post_edit"),
    path("donor_user/", blood_detail_user, name="user_donation"),
    path("donor_AP/", blood_detail_AP),
    path("donor_OP/", blood_detail_OP),
    path("donor_BP/", blood_detail_BP),
    path("donor_ON/", blood_detail_ON),
    path("donor_BN/", blood_detail_BN),
    path("donor_AN/", blood_detail_AN),
    path("donor_ABN/", blood_detail_ABN),
    path("blood_bank_create/", BloodBankCreateView, name="blood_bank_create"),
    path("blood_bank_list", blood_bank_list, name="bank_list"),
    path("blood_bank_list/<int:pk>/", blood_bank_detail, name="bank_list"),
    path("contact/", contact, name="contact"),
    path("thank/", TemplateView.as_view(template_name="thanks.html"), name="thank")

]
