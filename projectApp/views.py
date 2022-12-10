from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
# Create your views here.



class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



# class LoginAPIView(APIView):
#     serializer = LoginSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         # try:
#         serializer = self.serializer(data=request.data)
#         login_type = request.GET.get('loginType')
#         if serializer.is_valid(raise_exception=True):
#             email = serializer.data.get('email')
#             mobile_num = serializer.data.get('phoneNumber')
#             if email:
#                 user_data = User.objects.filter(email=email).values('username').last()
#                 user_name = user_data.get('username') if user_data else None
#             else:
#                 user_name = mobile_num
#             password = serializer.data.get('password')

#             if user_name:
#                 user = authenticate(username=user_name, password=password)
#                 if user and user.id:
#                     user_service = UserService()
#                     role_validation = user_service.validate_role(user, login_type)
#                     if role_validation == 2 or not login_type:
#                         return Response({"status": False, "message": "You are not allowed to login with this role"},
#                                         status=status.HTTP_400_BAD_REQUEST)
#                     elif role_validation == 0:
#                         user_service.add_user_role(user, login_type)
#                     data = user_service.get_login_creds(user, login_type)
#                     return Response({'data': data, 'status': True})

#         return Response({"status": False, "message": "please check your credentials"},
#                         status=status.HTTP_400_BAD_REQUEST)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



class EmployeeCreationAPIView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProjectCreationApiView(APIView):
    def post(self, request):
        serializer = projectDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def productListApiView(request):
    if request.method == 'GET':
        print(request.user.username)
        projects = ProjectDetails.objects.all()
        
        if projects:
            paginator = PageNumberPagination()
            paginator.page_size = 5
            projectsPagination = paginator.paginate_queryset(projects, request)
            projectDetailsInst = projectDetailSerializer(projectsPagination, many=True)
            projectDetailsInst = projectDetailsInst.data
            return paginator.get_paginated_response({'projectDetailsInst':projectDetailsInst})
        return Response({'msg':'No Data'})





