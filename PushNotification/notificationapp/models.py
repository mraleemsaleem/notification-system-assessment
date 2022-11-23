from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import uuid


# Models.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name



class ChannelType(models.Model):
    channel_name = models.CharField(max_length=100)

    def __str__(self):
        return self.channel_name



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    username        = models.CharField(max_length=30, unique=True)
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True, null=False, blank=False)
    phone           = models.IntegerField(blank=True, null=True)
    channell        = models.ManyToManyField(ChannelType,related_name="channelname_chn")
    category        = models.ForeignKey(Category,related_name="categoryname_cat",on_delete=models.CASCADE, blank=True, null=True)
    date_joined     = models.DateField(auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        if self.username:
            return self.username
        else:
            return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True



class LogHistory(models.Model):
    user       = models.ForeignKey(User,related_name="userlog",on_delete=models.CASCADE, blank=True, null=True)
    category   = models.ForeignKey(Category,related_name="categorylog",on_delete=models.CASCADE)
    channell   = models.ForeignKey(ChannelType, related_name="channellog", on_delete=models.CASCADE, blank=True,null=True)
    message    = models.TextField()
    send_data  = models.DateTimeField(auto_now_add=True, blank=True, null=True)