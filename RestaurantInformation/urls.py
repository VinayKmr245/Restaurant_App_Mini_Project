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
from django.urls import path
from RestaurantInformation import views as admins

urlpatterns = [
    path('AdminLoginCheck/', admins.AdminLoginCheck, name="AdminLoginCheck"),
    path('AdminHome/', admins.AdminHome, name="AdminHome"),
    path('AdminAddBranchUserForm/', admins.AdminAddBranchUserForm, name='AdminAddBranchUserForm'),
    path('AdminAddingBranchUserAction/', admins.AdminAddingBranchUserAction, name='AdminAddingBranchUserAction'),
    path('AdminSendingLoginDetails/', admins.AdminSendingLoginDetails, name='AdminSendingLoginDetails'),
    path('AdminSendingMailsToBrachUsers/', admins.AdminSendingMailsToBrachUsers, name='AdminSendingMailsToBrachUsers'),
    path('AdminViewAllReservations/', admins.AdminViewAllReservations, name="AdminViewAllReservations"),
    path("AdminViewRes/", admins.AdminViewRes, name="AdminViewRes"),
    path("AdminViewALLBillsForm/", admins.AdminViewALLBillsForm, name="AdminViewALLBillsForm"),
    path("AdminViewAllBranchBills/", admins.AdminViewAllBranchBills, name="AdminViewAllBranchBills"),




]
