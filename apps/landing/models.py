from django.db import models
from apps.core.models import CreatedModifiedAtDateTimeBase
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import models as authmodel
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class EmailLog(models.Model):
    """
    Model to log emails when users log in.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    email = models.EmailField(verbose_name='Email')
    login_time = models.DateTimeField(default=timezone.now, verbose_name='Login Time')

    def __str__(self):
        return f"{self.user.username} - {self.email} - {self.login_time}"

    class Meta:
        verbose_name = 'Email Log'
        verbose_name_plural = 'Email Logs'

class User(AbstractUser):
    bio = models.TextField(default='', null=True, blank=True)
    def __str__(self):
        return self.username

class YourModel(models.Model):
    class Meta:
        db_table = 'socialschema'
