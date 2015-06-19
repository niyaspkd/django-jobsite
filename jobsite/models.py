from django.db import models

import hashlib, datetime, random
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.


# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Jobs(models.Model):
 id = models.AutoField(primary_key=True)
 title=models.TextField()
 date= models.DateTimeField(default=timezone.now)
 location =  models.CharField(max_length=200)
 description=models.TextField()
 
 def __unicode__(self):
      return unicode(self.id )

class Apply(models.Model):

 
 name=models.CharField(max_length=200)
 email=models.EmailField()
 phone=models.CharField(max_length=200)
 description=models.TextField() 
 job_id= models.ForeignKey(Jobs)
 
 def __unicode__(self):
        return self.name



class MyUserManager(BaseUserManager):
    def create_user(self,username,first_name,last_name, email, password=None, role=1):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username,first_name=first_name,last_name=last_name,email=email,role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,first_name,last_name,email, role, password):
        user = self.create_user(username,first_name,last_name,email,password=password,role=role)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    ROLE_CHOICES = (
       ('1', 'Employer'),
       ('2', 'Employee'),
    )
    username      =   models.CharField(verbose_name='User Name',max_length=255,unique=True,)
    first_name    =   models.CharField(verbose_name='First Name', max_length=128, blank=False)
    last_name     =   models.CharField(verbose_name='Last Name', max_length=128, blank=False)
    email         =   models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    role          =   models.CharField(max_length=1,choices=ROLE_CHOICES)
    is_active     =   models.BooleanField(default=True)
    is_admin      =   models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email','role']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin




 
