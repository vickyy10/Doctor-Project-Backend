from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User,Doctor
from django.db.models import Q
from .serializer import UserRegistrationSerializer,UserSerializer,DoctorSerializer,MyTokenObtainPairSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

# Create your views here.

# =============TOKEN CUSTOMISATION===============


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer




# -------------- USER REGISTRATION ---------------------

from rest_framework import viewsets


class UserRegistrationView(viewsets.ViewSet):
    permission_classes=[AllowAny]

    def create(self,request):
        serializer=UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():

            user=User.objects.create_user(
            name = serializer.validated_data['name'],
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password'],
            is_doctor=serializer.validated_data['is_doctor'],

                )
            if user.is_doctor:
                Doctor.objects.create(
                    user=user,
                    name=serializer.validated_data['name'],
                    email=serializer.validated_data['email']
                )
            return Response({"msg":"user created","user datails":serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


# ----------------------------- USER --------------------------------------

# ============AFTER USER REGISTRATION=========
# see details of doctors
# crud user details



@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class UserHomeView(APIView):
    def get(self,request):
        data=Doctor.objects.all()
        serializer=DoctorSerializer(data,many=True)
        return Response(serializer.data)
    


# =======USER PROFILE EDIT===========

from rest_framework import viewsets

  
class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,req):
            print(req.user)
            data=User.objects.get(name=req.user)
            serializer=UserSerializer(data)
            return Response(serializer.data)
        
    def patch(self,request):
            data=User.objects.get(name=request.user)
            serializer=UserSerializer(data,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return 
        



# ------------------------- DOCTOR --------------------

class DoctorHomeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=request.user
        data=Doctor.objects.get(name=user)
        serializer=DoctorSerializer(data)
        return Response(serializer.data)


    def patch(self,request):
            print(request.data,'dataa')
            doctor=Doctor.objects.get(name=request.user)
            serializer=DoctorSerializer(doctor,data=request.data,partial=True)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                User.objects.filter(name=request.user).update(
                        name=request.data.get('name'),
                        email=request.data.get('email')
                    )
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





# -------------ADMIN ------------

class AdminUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
   
    def get(self,request):
        data=User.objects.exclude(Q(is_admin=True) | Q(is_doctor=True) )
        serializer=UserSerializer(data,many=True)
        return Response(serializer.data)
    
    def patch(self,request,pk=None):
        if pk is not None:
            print(request.data)
            user=User.objects.get(email=request.data['email'])
            serializer=UserSerializer(user,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        

class AdminDoctorView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
     
    def get(self,request):
        data=Doctor.objects.all()
        serializer=DoctorSerializer(data,many=True)
        return Response(serializer.data)
    

    def patch(self,request,pk=None):
        if pk is not None:
            print(request.data)
            user=User.objects.get(email=request.data['email'])
            serializer=UserSerializer(user,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                doctor=Doctor.objects.get(email=request.data['email'])
                serializer1=DoctorSerializer(doctor,data=request.data,partial=True)
                if serializer1.is_valid():
                    serializer1.save()
                    return Response(serializer1.data)
     


    
    
    

        









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

    
