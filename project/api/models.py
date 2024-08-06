from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,username,email,is_doctor,password=None,**extra_fields):
        if not email:
            raise ValueError('User Must Have an Email Address!!!')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_doctor=is_doctor
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    is_doctor=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD ='email'




class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=True,blank=True)
    departmet=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='media/doctor',null=True,blank=True)

    def __str__(self):
        return self.name
    
