from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,name,email,is_doctor,password=None,**extra_fields):
        if not email:
            raise ValueError('User Must Have an Email Address!!!')
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            is_doctor=is_doctor
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,is_doctor=False):
        user = self.create_user(
            email=email,
            password=password,
            is_doctor=is_doctor
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    is_doctor=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD ='email'

    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    hospital=models.CharField(max_length=100,null=True,blank=True)
    department=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='media/doctor',null=True,blank=True)




    
    
