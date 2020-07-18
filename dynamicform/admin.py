from django.contrib import admin

from dynamicform.models import *

# Register your models here.
admin.site.register(DynamicFormMaster),
admin.site.register(DynamicFormField),
admin.site.register(DynamicFormFieldDropdown),
admin.site.register(DynamicFormRelateWithAccountAndBranch),
admin.site.register(DynamicFormValue),
admin.site.register(FeedbackBackgroundImage),
admin.site.register(FeedbackLayout),


