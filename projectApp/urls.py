from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name="projectApp"

urlpatterns = [
    path('register-user/', views.RegisterAPIView.as_view(), name="registerUserUrl"),
    path('employee/create/', views.EmployeeCreationAPIView().as_view(), name="EmployeeCreationApiUrl"),
    path('projectDetail/create/', views.ProjectCreationApiView.as_view(), name="ProjectCreationApiUrl"),
    path('login/', views.MyObtainTokenPairView.as_view(), name="MyObtainTokenPairUrl"),
    path('login/refresh/',TokenRefreshView.as_view(), name="TokenRefreshUrl"),
    path('project-list/', views.productListApiView, name="projectlisturl")
]