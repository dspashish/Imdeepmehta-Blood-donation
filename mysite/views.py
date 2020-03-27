from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
from .forms import DonateBloodForm, BloodBanksForms
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from .models import DonateBlood, BloodBanks, Contact
from users.models import Profile


# Create your views here.
def homepage(request):
    template_name = "home.html"
    prof = Profile.objects.all()
    if request.user.is_authenticated:

        user = get_object_or_404(User, username=request.user)
        data = DonateBlood.objects.filter(author=user)
        context = {"data": data, "profile": prof}
    else:
        context = {"profile": prof}

    return render(request, template_name=template_name, context=context)


def register(request):
    if request.method == "POST":
        fist_name = request.POST["first_name"]
        last_name = request.POST['last_name']
        username = request.POST['username']

        password1 = request.POST['password1']

        password2 = request.POST['password2']

        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                context = {"message": "Username taken"}
                return render(request, template_name="registration.html", context=context)
            elif User.objects.filter(email=email).exists():
                context = {"message": "Email Taken"}
                return render(request, template_name="registration.html", context=context)
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=fist_name, last_name=last_name)
                user.save()
                return redirect('creator')

        else:
            context = {"message": "Password Not Matching"}
            return render(request, template_name="registration.html", context=context)

        print("User Created")
        return redirect("/")

    else:

        return render(request, template_name="registration.html")


def login(request):
    message = None

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:

            auth.login(request, user)

            return redirect("home")
        else:
            message = "Invalid Credentials"
            context = {"message": message}

            return render(request, template_name="login.html", context=context)


    else:
        return render(request, template_name="login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")


def creatorlogin(request):
    message = None

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user = get_object_or_404(User, username=request.user)

            a = Profile.objects.create(user=user)

            return redirect("donor_detail")
        else:
            message = "Invalid Credentials"
            context = {"message": message}

            return render(request, template_name="creatorlogin.html", context=context)


    else:
        return render(request, template_name="creatorlogin.html")


@login_required(login_url="/login/")
def donor_detail(request):
    form = DonateBloodForm()
    errors = None
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            form = DonateBloodForm(request.POST)
            if form.is_valid():
                obj = DonateBlood.objects.create(
                    author=user,
                    author2=user,
                    name=form.cleaned_data.get("name"),
                    dateofbirth=form.cleaned_data.get("dateofbirth"),
                    weight=form.cleaned_data.get("weight"),
                    blood_group=form.cleaned_data.get("blood_group"),
                    last_donation=form.cleaned_data.get("last_donation"),
                    frequency=form.cleaned_data.get("frequency"),
                    email=form.cleaned_data.get('email'),
                    gender=form.cleaned_data.get("gender"),
                    mobile_no=form.cleaned_data.get('mobile_no'),
                    address=form.cleaned_data.get("address"),
                    zip_code=form.cleaned_data.get("zip_code"),
                    message=form.cleaned_data.get("message")

                )
                return redirect("home")
        else:
            return redirect("login")

        if form.errors:
            print(form.errors)
            errors = form.errors

    context = {"form": form, "errors": errors, "name": request.user.first_name, "email": request.user.email}

    return render(request, template_name="form.html", context=context)


def blood_list(request):
    template_name = "donors_list.html"
    data = DonateBlood.objects.all()
    context = {
        "object_list": data
    }
    return render(request, template_name=template_name, context=context)


def blood_detail(request, pk):
    obj = DonateBlood.objects.get(pk=pk)
    if request.user.username == obj.author:
        context = {"object": obj, "true": True}
    else:
        context = {"object": obj}
    print(context)
    print(request.user.username)
    print(obj.author)

    return render(request, template_name="donor_detail.html", context=context)


def blood_detail_user(request):
    user = request.user.username

    obj = DonateBlood.objects.filter(author2=user)
    context = {
        "object_list": obj,

    }
    return render(request, template_name="user_donated_blood.html", context=context)


def blood_update(request, pk):
    obj = DonateBlood.objects.get(pk=pk)
    if request.method == "POST":
        if request.user.username == obj.author2:
            obj.name = request.POST.get("name")
            obj.dateofbirth = request.POST.get("dateofbirth")
            obj.weight = request.POST.get("weight")
            obj.blood_group = request.POST.get("blood_group")
            obj.last_donation = request.POST.get("last_donation")
            obj.frequency = request.POST.get("frequency")
            obj.email = request.POST.get("email")
            obj.mobile_no = request.POST.get("mobile_no")
            obj.address = request.POST.get("address")
            obj.zip_code = request.POST.get('zip_code')
            obj.gender = request.POST.get("gender")
            obj.save()
            return redirect("/donor_user/")
        else:
            return redirect("/donor_user/")

    else:
        return render(request, template_name="form.html", context={"obj": obj})


def blood_detail_ABP(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="AB+")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def blood_detail_AP(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="A+")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def blood_detail_OP(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="O+")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def blood_detail_BP(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="B+")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def blood_detail_ON(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="O-")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def blood_detail_BN(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="B-")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def blood_detail_AN(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="A-")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def blood_detail_ABN(request):
    obj = DonateBlood.objects.filter(blood_group__iexact="AB-")
    context = {
        "object_list": obj
    }
    return render(request, template_name="donors_list.html", context=context)


def BloodBankCreateView(request):
    form = BloodBanksForms()

    if request.method == "POST":
        bank_name = request.POST["blood_bank_name"]
        person = request.POST['contact_person']
        email = request.POST["email"]
        phone = request.POST["phone"]
        country = request.POST["country"]
        address = request.POST["address"]
        about = request.POST["about"]
        a = BloodBanks.objects.create(blood_bank_name=bank_name,
                                      contact_person=person,
                                      email=email,
                                      phone=phone,
                                      country=country,
                                      address=address,
                                      about=about)
        return redirect("home")

    context = {"form": form}
    return render(request, template_name="blood_bank_create.html", context=context)


def blood_bank_list(request):
    template_name = "banks_list.html"
    data = BloodBanks.objects.all()
    context = {
        "object_list": data
    }
    return render(request, template_name=template_name, context=context)


def blood_bank_detail(request, pk):
    obj = BloodBanks.objects.get(pk=pk)

    context = {"object": obj}

    return render(request, template_name="blood_detail.html", context=context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        a = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect("thank")
    return render(request, template_name="contact.html")
