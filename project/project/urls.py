"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import  DefaultRouter
from api.views import UserRegistrationView,UserHomeView,UserProfileView,DoctorHomeView,AdminUserView,AdminDoctorView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from api.views import MyTokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings

router=DefaultRouter()
router.register(r'UserRegistration',UserRegistrationView,basename='UserRegistration')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('userhome/',UserHomeView.as_view(),name='userhome'),
    path('Login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/',AdminUserView.as_view(),name='users'),
    path('api/users/<int:pk>/',AdminUserView.as_view(),name='usersblock'),
    path('api/doctors/',AdminDoctorView.as_view(),name='doctors'),
    path('api/doctors/<int:pk>/',AdminDoctorView.as_view(),name='doctors'),
    path('DoctorHome/',DoctorHomeView.as_view(),name='DoctorHome'),
    path('UserProfile/',UserProfileView.as_view(),name='UserProfile')
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


