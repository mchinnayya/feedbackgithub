from django.db import models
from organization.models import Organization
from django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    otp = models.IntegerField(default=1)
    active = models.SmallIntegerField(default=1)       # 1 means Active, 0 means Inactive
    two_step_varification = models.SmallIntegerField(default=0)      # 1 means Yes, 0 means No
    mobile = models.BigIntegerField()
    gender = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.IntegerField() # 0 means Admin, 1 User
    api_token = models.CharField(max_length=60, null=True, blank=True)
    remember_token = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user



