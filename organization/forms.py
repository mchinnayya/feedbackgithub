from django import forms


from organization.models import Organization


class OrganizationForm(forms.ModelForm):
    organization_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Organization Name'}), label="Organization Name", required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter City Name'}), label="City", required=True)
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter State Name'}), label="State", required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter Country Name'}), label="Country", required=True)

    class Meta:
        model = Organization
        fields = ('organization_name', 'city', 'state', 'country',)


