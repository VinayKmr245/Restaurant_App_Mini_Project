import datetime as dt
import json
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from RestaurantInformation.models import BranchUserRegisterModel

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            request = self.context["request"]
        except KeyError:
            pass
        else:
            request_data=json.load(request.body)
            username=request_data.get("username")
            password=request_data.get("password")
            login_has_expired = False
            try:
                login=BranchUserRegisterModel.objects.get(loginid=username,password=password)
            except BranchUserRegisterModel.DoesNotExist:
                login_has_expired = True
                error_message="this login has expire"
                error_name="expire profile"
                raise exceptions.AuthenticationFailed(error_message,error_name)
            finally:
                return super().validate(attrs)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
