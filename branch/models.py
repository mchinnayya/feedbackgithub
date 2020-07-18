from django.db import models
from django.urls import reverse
from organization.models import Organization
from account.models import Account
# Create your models here.
class Branch(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=191)
    branch_name = models.CharField(max_length=191)
    parent_id = models.IntegerField(null=True, default=0)
    type = models.IntegerField()
    city = models.CharField(max_length=191)
    state = models.CharField(max_length=191)
    country = models.CharField(max_length=191)
    branch_code = models.CharField(max_length=191, default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.branch_name
