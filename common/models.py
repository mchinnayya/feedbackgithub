from django.db import models

# Create your models here.
class Lookup(models.Model):
    lookup_identifier = models.BigIntegerField(null=False)
    name = models.CharField(max_length=255, null=False)
    lookup_value = models.CharField(max_length=255, null=False)
    parent_lookup = models.BigIntegerField(null=True)

    def __str__(self):
        return self.lookup_value
