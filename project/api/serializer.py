from rest_framework import serializers
from.models import User,Doctor

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirmpassword=serializers.CharField(max_length=20)


    class Meta:
        model=User
        fields=['name','email','password','confirmpassword','is_doctor',]


    def validate(self,data):

        name=data['name']
        password=data['password']
        email=data['email']
        confirmpassword=data['confirmpassword']
        chr='!@#$%^&*()_+'



        if any(i in chr for i in name):
            raise serializers.ValidationError('remove special character from name')
        

        
        if password != confirmpassword:

            raise serializers.ValidationError('password does not match')
        
        return data
    
    


class UserloginSerializer(serializers.Serializer):
    Lemail=serializers.EmailField()
    Lpassword=serializers.CharField()

    def validate(self,data):
        try:
            obj=User.objects.get(email=data['Lemail'])
            if obj:
                print(obj)
                if data['Lpassword'] == obj.password:
                    raise serializers.ValidationError("password and username matched")
                else:
                    raise serializers.ValidationError("password deos not match")
        except User.DoesNotExist:
            raise serializers.ValidationError("email does not exist.")

        
        



class UserSerializer(serializers.ModelSerializer):


    class Meta:

        model=User
        fields='__all__'


class DoctorSerializer(serializers.Serializer):

    class Meta:
        model:Doctor
        fields='__all__'
    







