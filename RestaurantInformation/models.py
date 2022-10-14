from django.db import models
from django.contrib.auth.models import UserManager
# Create your models here.
class BranchUserRegisterModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    USERNAME_FIELD = 'loginid'
    REQUIRED_FIELDS = ['password']
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)

    objects=UserManager()

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'BranchUsers'
