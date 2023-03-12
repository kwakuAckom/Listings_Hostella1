from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email is required.')
        email = self.normalize_email(email).lower()

        user = self.model(
            email = email,
            #name = name,
        )
        user.set_password(password)
        user.save()

        return user
    
    def create_realtor(self, email, password):
        user = self.create_user(email, password)
        user.is_realtor = True
        user.save()
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True, verbose_name= 'email address')
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_realtor = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
