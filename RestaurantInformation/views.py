from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import BranchuserRegisterForm
from .models import BranchUserRegisterModel
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
today = date.today()
from django.contrib.auth.models import User
from SlaveManagement.models import AddUserReservationModel,RestaurantBillModel
# Create your views here.

def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        elif usrid == 'Admin' and pswd == 'Admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})

def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def AdminAddBranchUserForm(request):
    form = BranchuserRegisterForm()
    return render(request, 'admins/AdminAddBranchUser.html',{'form':form})

def AdminAddingBranchUserAction(request):
    if request.method == 'POST':
        form = BranchuserRegisterForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            usrnmae = form.cleaned_data['loginid']
            pswd = form.cleaned_data['password']
            print("User name =",usrnmae, " Password  =",pswd)
            form.save()
            User.objects.create_user(username=usrnmae,password=pswd)
            messages.success(request, 'Branch User Register successfull')
            form = BranchuserRegisterForm()
            return render(request, 'admins/AdminAddBranchUser.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = BranchuserRegisterForm()
    return render(request, 'admins/AdminAddBranchUser.html', {'form': form})

def AdminSendingLoginDetails(request):
    data = BranchUserRegisterModel.objects.all()
    return render(request, 'admins/ViewAllBranchUsers.html',{'data':data})

def AdminSendingMailsToBrachUsers(request):
    id = request.GET.get('uid')
    print('Your ID is ',id)
    try:
        check = BranchUserRegisterModel.objects.get(id=id)
        loginname = check.loginid
        loginpass = check.password
        branch = check.branch
        email = check.email
        sub = "[" + str(today) + "]Login Details of the Branch " + branch
        mailbody = "Dear user, this is your login details of the Restaurant at our branch " + branch + "Login id " \
                                                                                                       "<loginname>" + \
                   loginname + "</loginname> and password is " + loginpass

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        obj = send_mail(sub, mailbody, email_from, recipient_list)
        print('Mail Object is ' + obj)


    except Exception as ex:
        #print("Error is ",str(ex))
        pass
    data = BranchUserRegisterModel.objects.all()
    return render(request, 'admins/ViewAllBranchUsers.html', {'data': data})


from rest_framework_jwt import authentication

class MyJWTAuthentication(authentication.JSONWebTokenAuthentication):
    user_model = 'RestaurantInformation.models.BranchUserRegisterModel'


def AdminViewAllReservations(request):
    return render(request, 'admins/AdminViewReservations.html',{})

def AdminViewRes(request):
    branch = request.POST.get('branch')
    data = AddUserReservationModel.objects.filter(branch=branch)
    return render(request, 'admins/AdminViewReservations.html', {'data':data})

def AdminViewALLBillsForm(request):
    return render(request,'admins/AdminViewAllBills.html',{})

def AdminViewAllBranchBills(request):
    branch = request.POST.get('branch')
    data = RestaurantBillModel.objects.filter(branch=branch)
    return render(request, 'admins/AdminViewAllBills.html', {'data': data})
