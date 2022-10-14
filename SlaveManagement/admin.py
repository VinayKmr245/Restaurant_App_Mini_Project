from django.contrib import admin
from RestaurantInformation.models import BranchUserRegisterModel
# Register your models here.

class BranchUserRegisterAdmin(admin.ModelAdmin):
    list_display=('id','name','loginid','password','mobile','email','locality','address','city','state','branch')

admin.site.register(BranchUserRegisterModel,BranchUserRegisterAdmin)

from .models import AddUserReservationModel

class AddUserReservationAdmin(admin.ModelAdmin):
    list_display = ('custname', 'mobile', 'email','noofChairs','comingfrom','branch','reservDate','cdate')
admin.site.register(AddUserReservationModel,AddUserReservationAdmin)