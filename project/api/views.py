from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User,Doctor
from .serializer import UserRegistrationSerializer,UserSerializer,DoctorSerializer,UserloginSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

# -------------- USER REGISTRATION ---------------------

from rest_framework import viewsets

class UserRegistrationView(viewsets.ViewSet):

    def create(self,request):
        print(request.data)
        serializer=UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():

            User.objects.create(
            name = serializer.validated_data['name'],
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password'],
            is_doctor=serializer.validated_data['is_doctor'],

                )
            return Response({"msg":"user created","user datails":serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

# ----------------- USER LOGIN ------------------------

class UserLogin(APIView):

    def post(self,request):
        data=request.data 
        serializer=UserloginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"user logined"})
        else:
            return Response(serializer.errors)
        

# ----------------------------- USER --------------------------------------

# ============AFTER USER REGISTRATION=========
# see details of doctors
# crud user details



class UserHomeView(APIView):

    def get(self,request):
        data=Doctor.objects.all()
        if data:
            serializer=UserSerializer(data,many=True)
            return Response(serializer.data)
        return Response({"msg":"no doctor available"})


# =======USER PROFILE EDIT===========

from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin  

class UserProfileView(viewsets.GenericViewSet,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):

    queryset=User.objects.all()
    serializer_class=UserSerializer


# ------------------------- DOCTOR --------------------

class DoctorHomeView(viewsets.ViewSet):

    def retrive(self,request,pk=None):
        if pk is not None:
            data=Doctor.objects.get(id=pk)
            serializer=DoctorSerializer(data)
            return Response(serializer.data)



#============== DOCTOR PROFILE EDIT========
 
class DoctorProfileView(viewsets.GenericViewSet,UpdateModelMixin,RetrieveModelMixin):

    queryset=User.objects.all()
    serializer_class=UserSerializer


# ============ ADMIN ===========

class AdminProfileView(viewsets.GenericViewSet,UpdateModelMixin,RetrieveModelMixin):

    queryset=User.objects.all()
    serializer_class=UserSerializer



class AdminUserView(APIView):

    def get(self,request):
        data=User.objects.all()
        serializer=UserSerializer(data)
        return Response(serializer.data)



class AdminDoctorView(APIView):
     
     def get(self,request):
        data=Doctor.objects.all()
        serializer=DoctorSerializer(data)
        return Response(serializer.data)
     


    
    
    

        









# ===========AFTER DOCTOR REGISTRATION=============
# see details on home page
#  edit my detail
# delete my account

# class DoctorView(viewsets.ViewSet):

#     def list(self,request):
#         data = Doctor.objects.all()
#         serializer=DoctorSerializer(data,many=True)
#         return Response(serializer.data)
    

#     def retrive(self,req,pk=None):
#         if pk is not None:
#             data=Doctor.objects.get(id=pk)
#             serializer=DoctorSerializer(data,many=False)
#             return Response(serializer.data)



#     def create(self,request):
#         data=request.data
#         if data:
#             serializer=DoctorSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"msg:":"data added","data":serializer.data},status=status.HTTP_200_OK)    
#         return Response('not added',status=status.HTTP_404_NOT_FOUND)
    


#     def update(self,request,pk=None):
#         if pk is not None:
#             obj=Doctor.objects.get(id=pk)
#             serializer=DoctorSerializer(obj,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()

    
