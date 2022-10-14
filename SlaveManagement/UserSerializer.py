from rest_framework import serializers
from RestaurantInformation.models import BranchUserRegisterModel
class BranchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchUserRegisterModel
        fields = '__all__'



from .models import AddUserReservationModel
class AddUserReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUserReservationModel
        fields = '__all__'


