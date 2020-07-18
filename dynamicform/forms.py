from django import forms
from dynamicform.models import *
from common.models import Lookup


class DynamicFormMasterForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), label="Title", required=True)
    description = forms.CharField(widget=forms.Textarea({'class': 'form-control'}), label="Description", required=True)

    class Meta:
        model = DynamicFormMaster
        fields = ('title', 'description')


class UserAssignForm(forms.ModelForm):
    user = Account.objects.values_list('user', flat=True)
    # user = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'style': "width: 100%"}), label="User", required=True)

    class Meta:
        model = Account
        fields = ('user',)

class DynamicFormValueForm(forms.ModelForm):
    mobile_number = forms.ImageField(widget=forms.NumberInput({'class': 'form-control'}), label="Mobile Number", required=True)

    class Meta:
        model = DynamicFormValue
        fields = ('mobile_number',)