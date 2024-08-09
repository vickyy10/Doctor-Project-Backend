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
from api.views import UserRegistrationView,UserHomeView,UserProfileView,DoctorHomeView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from api.views import MyTokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings

router=DefaultRouter()
router.register(r'UserRegistration',UserRegistrationView,basename='UserRegistration')
router.register(r'UserProfile',UserProfileView,basename='UserProfile')
router.register(r'DoctorHome',DoctorHomeView,basename='DoctorHome')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('userhome/',UserHomeView.as_view(),name='userhome'),
     path('Login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


