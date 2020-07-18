from django.db import models


# Create your models here.

class Organization(models.Model):
    organization_name = models.CharField(max_length=191)
    created_by = models.CharField(max_length=191)
    city = models.CharField(max_length=191)
    state = models.CharField(max_length=191)
    country = models.CharField(max_length=191)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.organization_name
