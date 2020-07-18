from django import forms
from branch.models import Branch
from common.models import Lookup
from organization.models import Organization


class BranchForm(forms.ModelForm):
    organization = forms.ModelChoiceField(queryset=Organization.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'style': "width: 100%"}), label="Organization", required=True)
    branch_name = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="Branch Name", required=True)
    parent_id = forms.ModelChoiceField(queryset=Branch.objects.all(), widget=forms.Select({'class':'form-control'}),
                                       label="Parent Id", required=False)
    type = forms.ModelChoiceField(queryset=Lookup.objects.filter(lookup_identifier=109), widget=forms.Select(
        attrs={'class': 'form-control', 'style': "width: 100%"}), label="Type", required=True)
    city = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="City", required=True)
    state = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="State", required=True)
    country = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="Country", required=True)
    branch_code = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="Branch Code", required=True)

    class Meta:
        model = Branch
        fields = ('branch_name', 'organization', 'parent_id', 'type', 'city', 'state', 'country', 'branch_code')