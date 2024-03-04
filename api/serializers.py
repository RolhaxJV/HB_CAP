# serializers.py
from rest_framework import serializers
from app.models import D_Date,D_Depart,D_Type,F_Dose

# region FAIT
class F_Dose_Serializer(serializers.ModelSerializer):
    class Meta:
        model = F_Dose
        fields = '__all__'

# endregion

# region DIMENSION
class D_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Type
        fields = '__all__'

class D_Date_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Date
        fields = '__all__'

class D_Depart_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Depart
        fields = '__all__'

# endregion