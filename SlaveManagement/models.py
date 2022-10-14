from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from rest_framework_jwt import authentication

class MyJWTAuthentication(authentication.JSONWebTokenAuthentication):
    user_model = 'RestaurantInformation.models.BranchUserRegisterModel'

import datetime
class AddUserReservationModel(models.Model):
    custname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    noofChairs = models.IntegerField()
    comingfrom = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    reservDate = models.DateField()
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.custname
    class Meta:
        db_table = 'CustomerReserv'

class RestaurantBillModel(models.Model):
    customername = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    noofchairs = models.CharField(max_length=100)
    itemcodes = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    totalamount = models.FloatField()
    branchUser = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customername

    class Meta:
        db_table = 'BillTable'
