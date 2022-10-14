from django.shortcuts import render,HttpResponse
from .UserSerializer import BranchUserSerializer
from django.contrib import messages

import requests
# Create your views here.
def BranchUserLoginForm(request):
    return render(request,"BranchUsersLoginForm.html",{})
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': BranchUserSerializer(user, context={'request': request}).data
    }
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from RestaurantInformation.models import BranchUserRegisterModel
from .models import AddUserReservationModel,RestaurantBillModel
class BranchUserCrudView(ModelViewSet):
    queryset = BranchUserRegisterModel.objects.all()
    serializer_class = BranchUserSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

url ='http://localhost:8000/sm/br/reserv/'


def BranchUserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        branch = request.POST.get('branch')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = BranchUserRegisterModel.objects.get(loginid=loginid, password=pswd, branch=branch)
            if check.id != 0:
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['password'] = check.password
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                request.session['branch'] = check.branch
                return render(request, 'slaves/BranchUserHome.html', {})
            else:
                messages.success(request, 'Your Not Authenticated')
                return render(request, 'BranchUsersLoginForm.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'BranchUsersLoginForm.html', {})

def SlavesHome(request):
    return render(request, 'slaves/BranchUserHome.html', {})

def GetTokenBranchUser(request):
    password = request.session['password']
    username = request.session['loginid']
    import json
    data = {'username':username, 'password':password}
    url = 'http://localhost:8000/sm/auth-jwt/'
    x = requests.post(url, json=data)
    x = x.json()
    print(type(x))
    print("token =",x['token'])
    request.session['token'] = x['token']
    return render(request,'slaves/SlaveToken.html',{})


from rest_framework.viewsets import ModelViewSet
from .models import AddUserReservationModel
from .UserSerializer import AddUserReservationSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomerReserveCRUDCBV(ModelViewSet):
    queryset = AddUserReservationModel.objects.all()
    serializer_class = AddUserReservationSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

def GetReservations(request):
    password = request.session['password']
    username = request.session['loginid']
    token = request.session['token']
    import json
    #data = {"Authorization": "jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ1c2VybmFtZSI6ImFsZXgiLCJleHAiOjE2MDI3MzkzMjAsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE2MDI3MzkwMjB9.w7kWJWOEeUXMxuiOMNQPohXuPj1PIr8gvXrg7lefexA"}
    #headers = {'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ1c2VybmFtZSI6ImFsZXgiLCJleHAiOjE2MDI3MzkzMjAsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE2MDI3MzkwMjB9.w7kWJWOEeUXMxuiOMNQPohXuPj1PIr8gvXrg7lefexA'}
    #x = requests.get(url,json=data)
    branch = request.session['branch']
    PARAMS = {'branch':branch}
    x = requests.get(url, headers = {'Authorization': 'jwt '+token}, params = PARAMS)
    code = x.status_code
    msg= ''
    data = {}
    if code==401:
        msg= "Signature has expired"
    else:
        data = AddUserReservationModel.objects.filter(branch=branch)
    text = x.text
    x = x.json()
    #print(x)

    return render(request, 'slaves/ViewAllReservations.html', {'data': data, 'code': code, 'msg': msg})
    #return render(request, 'slaves/ViewAllReservations.html',{'data':x,'code':code,'msg':msg})

def SlaveDoNewBookingForm(request):
    return render(request, 'slaves/NewReservationtoCust.html',{})

def NewBookingStore(request):
    if request.method=='POST':
        custName = request.POST.get('custname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        noofchairs = request.POST.get('noofchairs')
        comingfrom = request.POST.get('comingfrom')
        brnach = request.POST.get('brnach')
        reservDate = request.POST.get('reservDate')
        data = {'custname': custName, 'mobile': mobile, 'email': email, 'noofChairs': noofchairs,'comingfrom': comingfrom,'branch': brnach,'reservDate': reservDate}
        token = request.session['token']
        x = requests.post(url, headers = {'Authorization': 'jwt '+token},json=data)
        code = x.status_code
        msg = ''
        if code == 401:
            msg = "Signature has expired"
        x = x.json()
        print(x)
    return render(request, 'slaves/NewReservationtoCust.html',{"code":code,'msg':msg})

def DeleteReservation(request):
    id = request.GET.get('id')
    token = request.session['token']
    data = {"id":id}
    x = requests.delete(url+""+id, headers={'Authorization': 'jwt ' + token})
    code = x.status_code
    print("Status Code",code)
    return render(request, 'slaves/BranchUserHome.html', {})

def ReservationEditUpdate(request):
    id = request.GET.get('id')
    token = request.session['token']
    data = {"id": id}
    x = requests.get(url + "" + id, headers={'Authorization': 'jwt ' + token})
    code = x.status_code
    print("Status Code", code)
    x = x.json()
    print("Response ",x)
    return render(request,'slaves/UpdateReservation.html',{'data':x})

def UpdateReservationAction(request):
    if request.method=='POST':
        id = request.POST.get('id')
        custName = request.POST.get('custname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        noofchairs = request.POST.get('noofchairs')
        comingfrom = request.POST.get('comingfrom')
        brnach = request.POST.get('brnach')
        reservDate = request.POST.get('reservDate')
        data = {'custname': custName, 'mobile': mobile, 'email': email, 'noofChairs': noofchairs,'comingfrom': comingfrom,'branch': brnach,'reservDate': reservDate}
        token = request.session['token']
        x = requests.put(url+""+id+"/", headers = {'Authorization': 'jwt '+token},json=data)
        code = x.status_code
        msg = ''
        if code == 401:
            msg = "Signature has expired"

    return render(request, 'slaves/BranchUserHome.html',{"code":code,'msg':msg})

def GenerateBillingForm(request):
    return render(request,"slaves/GenerateBill.html",{})

def BillDataStored(request):
    if request.method=='POST':
        customername = request.POST.get('custname')
        mobile = request.POST.get('mobile')
        noofchairs = request.POST.get('noofchairs')
        itemcodes = request.POST.get('itemcodes')
        branch = request.POST.get('branch')
        totalamount = request.POST.get('totalamount')
        username = request.session['loginid']
        RestaurantBillModel.objects.create(customername=customername,mobile=mobile,noofchairs=noofchairs,itemcodes=itemcodes,branch=branch,totalamount=totalamount,branchUser=username)
        messages.success(request, 'Bill Data Stored Success')
        return render(request, "slaves/GenerateBill.html", {})

def ViewBranchBills(request):
    branch = request.session['branch']
    data = RestaurantBillModel.objects.filter(branch=branch)
    return render(request,"slaves/SlaveViewAllBills.html",{'data':data})