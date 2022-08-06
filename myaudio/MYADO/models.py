from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
class Audio_Store(models.Model):
    record = models.FileField(upload_to='documents/',null=False,unique=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user',verbose_name='owner')
    class Meta:
        db_table = 'Audio_Store'

