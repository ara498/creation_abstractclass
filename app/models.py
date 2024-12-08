from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
class UserProfileManager(BaseUserManager):
    def create_user(self,email,f_n,l_n,password=None):
        if not email:
            raise ValueError('email is not')
        nemail=self.normalize_email(email)
        UO=self.model(email=nemail,f_n=f_n,l_n=l_n)
        UO.set_password(password)
        UO.save()
        return UO

    def create_superuser(self,email,f_n,l_n,password):
        NUO=self.create_user(email,f_n,l_n,password)
        NUO.is_staff=True
        NUO.is_superuser=True
        NUO.save()


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    f_n=models.CharField(max_length=100)
    l_n=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['f_n','l_n']                
