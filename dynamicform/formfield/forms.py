from django import forms
from dynamicform.models import *
from common.models import Lookup


class DynamicFormFieldForm(forms.ModelForm):

    field_title = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="Field Title", required=True)
    field_type = forms.ModelChoiceField(queryset=Lookup.objects.filter(lookup_identifier=110), widget=forms.Select(
        attrs={'class': 'form-control kt_select2', 'style': "width: 100%", 'onchange':'onfieldtypeSelected(this.value)'}), label="Field Type", required=True)
    field_hidden = forms.ModelChoiceField(queryset=Lookup.objects.filter(lookup_identifier=111), widget=forms.Select(
        attrs={'class': 'form-control kt_select2', 'style': "width: 100%"}), label="Field Hidden", required=True)
    field_description = forms.CharField(widget=forms.Textarea({'class':'form-control'}), label="Field Description", required=True)

    class Meta:
        model = DynamicFormField
        fields = ('field_title', 'field_type', 'field_hidden', 'field_description')

class DynamicFormFieldDropdownForm(forms.ModelForm):
    dropdown_label = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), label="Value (Dropdown, Star, Emoji, Slider, radio) <br/><small>Please enter comma seperated value like Male,Female</small>", required=True)

    class Meta:
        model = DynamicFormFieldDropdown
        fields = ('dropdown_label',)

