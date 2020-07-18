from django.db import models
from account.models import Account, User
from branch.models import Branch
from organization.models import Organization


# Create your models here.


class DynamicFormMaster(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)
    form_url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DynamicFormField(models.Model):
    dynamic_field_master = models.ForeignKey(DynamicFormMaster, on_delete=models.CASCADE)
    field_title = models.CharField(max_length=255)
    field_description = models.CharField(max_length=500, default=True)
    field_type = models.IntegerField()
    field_original_name = models.CharField(max_length=50, null=True, blank=True)
    field_hidden = models.SmallIntegerField(default=0)
    field_order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.dynamic_field_master


class DynamicFormRelateWithAccountAndBranch(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    dynamic_form_master = models.ForeignKey(DynamicFormMaster, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.user


class DynamicFormFieldDropdown(models.Model):
    dynamic_form_field = models.ForeignKey(DynamicFormField, on_delete=models.CASCADE)
    dropdown_label = models.CharField(max_length=255)
    dropdown_value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.dynamic_form_field


class FeedbackBackgroundImage(models.Model):
    form_master = models.ForeignKey(DynamicFormMaster, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=255)
    imageUrl = models.ImageField(upload_to='images/', blank=True, null=True)
    image_name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.form_master

class FeedbackLayout(models.Model):
    form_master = models.ForeignKey(DynamicFormMaster, on_delete=models.CASCADE)
    description_left_1 = models.TextField(max_length=1000, null=True)
    description_left_2 = models.TextField(max_length=1000, null=True)
    description_left_3 = models.TextField(max_length=1000, null=True)
    description_right_1 = models.TextField(max_length=1000, null=True)
    description_right_2 = models.TextField(max_length=1000, null=True)
    description_right_3 = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.form_master

class DynamicFormValue(models.Model):
    form_master = models.ForeignKey(DynamicFormMaster, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    mobile_number = models.BigIntegerField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    dfcustom_1 = models.CharField(max_length=10, null=True)
    dfcustom_2 = models.CharField(max_length=10, null=True)
    dfcustom_3 = models.CharField(max_length=10, null=True)
    dfcustom_4 = models.CharField(max_length=10, null=True)
    dfcustom_5 = models.CharField(max_length=10, null=True)
    dfcustom_6 = models.CharField(max_length=10, null=True)
    dfcustom_7 = models.CharField(max_length=10, null=True)
    dfcustom_8 = models.CharField(max_length=10, null=True)
    dfcustom_9 = models.CharField(max_length=10, null=True)
    dfcustom_10 = models.CharField(max_length=10, null=True)
    dfcustom_11 = models.CharField(max_length=10, null=True)
    dfcustom_12 = models.CharField(max_length=10, null=True)
    dfcustom_13 = models.CharField(max_length=10, null=True)
    dfcustom_14 = models.CharField(max_length=10, null=True)
    dfcustom_15 = models.CharField(max_length=10, null=True)
    dfcustom_16 = models.CharField(max_length=10, null=True)
    dfcustom_17 = models.CharField(max_length=10, null=True)
    dfcustom_18 = models.CharField(max_length=10, null=True)
    dfcustom_19 = models.CharField(max_length=10, null=True)
    dfcustom_20 = models.CharField(max_length=10, null=True)
    dfcustom_21 = models.CharField(max_length=10, null=True)
    dfcustom_22 = models.CharField(max_length=10, null=True)
    dfcustom_23 = models.CharField(max_length=10, null=True)
    dfcustom_24 = models.CharField(max_length=10, null=True)
    dfcustom_25 = models.CharField(max_length=10, null=True)
    dfcustom_26 = models.CharField(max_length=10, null=True)
    dfcustom_27 = models.CharField(max_length=10, null=True)
    dfcustom_28 = models.CharField(max_length=10, null=True)
    dfcustom_29 = models.CharField(max_length=10, null=True)
    dfcustom_30 = models.CharField(max_length=10, null=True)
    dfcustom_31 = models.CharField(max_length=10, null=True)
    dfcustom_32 = models.CharField(max_length=10, null=True)
    dfcustom_33 = models.CharField(max_length=10, null=True)
    dfcustom_34 = models.CharField(max_length=10, null=True)
    dfcustom_35 = models.CharField(max_length=10, null=True)
    dfcustom_36 = models.CharField(max_length=10, null=True)
    dfcustom_37 = models.CharField(max_length=10, null=True)
    dfcustom_38 = models.CharField(max_length=10, null=True)
    dfcustom_39 = models.CharField(max_length=10, null=True)
    dfcustom_40 = models.CharField(max_length=10, null=True)
    dfcustom_41 = models.CharField(max_length=10, null=True)
    dfcustom_42 = models.CharField(max_length=10, null=True)
    dfcustom_43 = models.CharField(max_length=10, null=True)
    dfcustom_44 = models.CharField(max_length=10, null=True)
    dfcustom_45 = models.CharField(max_length=10, null=True)
    dfcustom_46 = models.CharField(max_length=10, null=True)
    dfcustom_47 = models.CharField(max_length=10, null=True)
    dfcustom_48 = models.CharField(max_length=10, null=True)
    dfcustom_49 = models.CharField(max_length=10, null=True)
    dfcustom_50 = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.form_master




