from rest_framework import serializers
from django.contrib.auth.models import User
from projectApp.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = "__all__"


class projectDetailSerializer(serializers.ModelSerializer):
    projectManagerEmail = serializers.SerializerMethodField()
    projectManagerName = serializers.SerializerMethodField()
    empDetails = serializers.SerializerMethodField()

    def get_projectManagerEmail(self, obj):
        return obj.projectManager.email

    def get_projectManagerName(self, obj):
        return obj.projectManager.name

    def get_empDetails(self, obj):
        detailList = {}
        email = obj.projectManager.email
        name = obj.projectManager.name
        doj = obj.projectManager.doj

        detailList["email"] = email
        detailList["name"] = name
        detailList["date of joining"] = doj
        return detailList

    class Meta:
        model = ProjectDetails
        fields = ["projectName","projectStartDate","projectEndDate","projectManager","employeeName", "projectManagerEmail", "projectManagerName", "empDetails"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, min_length=6, max_length=68, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=False)
#     phoneNumber = serializers.CharField(required=False)
#     countryCode = serializers.CharField(required=False)
#     password = serializers.CharField(max_length=60, min_length=6)

#     class Meta:
#         model = User
#         fields = ['id', 'usrname', 'password']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token




