"""RestaurantBilling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from SlaveManagement import views as slaves
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as vs
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from SlaveManagement import views as v
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

router = DefaultRouter()
router.register('reserv',v.CustomerReserveCRUDCBV)

# obtain_jwt_token = ObtainJSONWebToken.as_view(user_model='RestaurantInformation.BranchUserRegisterModel')
# obtain_jwt_token = ObtainJSONWebToken.as_view(user_model='SlaveManagement.MyJWTAuthentication')


urlpatterns = [
    path('BranchUserLoginForm/', slaves.BranchUserLoginForm, name="BranchUserLoginForm"),
    path('get-api-token/',vs.ObtainAuthToken,name='get-api-token'),
    path('br/',include(router.urls)),
    path('auth-jwt/',obtain_jwt_token),
    #path('auth-jwt/',TokenObtainPairView),
    path('auth-jwt-refresh/',refresh_jwt_token),
    path('auth-jwt-verify/',verify_jwt_token),
    #path('api-token-auth/', obtain_jwt_token, name='auth-jwt-get')

    path('BranchUserLoginCheck/', slaves.BranchUserLoginCheck, name="BranchUserLoginCheck"),
    path('SlavesHome/', slaves.SlavesHome, name='SlavesHome'),
    path('GetTokenBranchUser/', slaves.GetTokenBranchUser, name="GetTokenBranchUser"),
    path('GetReservations/', slaves.GetReservations, name="GetReservations"),
    path('SlaveDoNewBookingForm/', slaves.SlaveDoNewBookingForm, name="SlaveDoNewBookingForm"),
    path('NewBookingStore/', slaves.NewBookingStore, name="NewBookingStore"),
    path("DeleteReservation/", slaves.DeleteReservation, name="DeleteReservation"),
    path("ReservationEditUpdate/", slaves.ReservationEditUpdate, name="ReservationEditUpdate"),
    path("UpdateReservationAction/", slaves.UpdateReservationAction, name="UpdateReservationAction"),
    path("GenerateBillingForm/", slaves.GenerateBillingForm, name="GenerateBillingForm"),
    path("BillDataStored/", slaves.BillDataStored, name="BillDataStored"),
    path("ViewBranchBills/", slaves.ViewBranchBills, name="ViewBranchBills"),







]
