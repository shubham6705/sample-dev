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





