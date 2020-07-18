from django import forms
from account.models import Account
from common.models import Lookup
from account.models import User
from organization.models import Organization
from role.models import UserRole

choice = [('0', 'admin'), ('1', 'user'), ]
activeChoice = [('0', 'Inactive'), ('1', 'Active'), ]


class AccountForm(forms.ModelForm):
    mobile = forms.IntegerField(widget=forms.NumberInput({'class': 'form-control'}), label="Mobile", required=True)
    gender = forms.ModelChoiceField(queryset=Lookup.objects.filter(lookup_identifier=100), widget=forms.Select(
        attrs={'class': 'form-control kt_select2', 'style': "width: 100%"}), label="Gender", required=True)
    start_date = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), )
    end_date = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))
    organization = forms.ModelChoiceField(queryset=Organization.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'style': "width: 100%"}), label="Organization", required=True)
    active = forms.IntegerField(label="Status", required=True, widget=forms.Select(choices=activeChoice,
                                                                                   attrs={
                                                                                       'class': 'form-control'}))  # 1 means Active, 0 means Inactive
    role = forms.CharField(label='Role', required=True,
                           widget=forms.Select(choices=choice, attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('mobile', 'gender', 'start_date', 'end_date', 'role', 'user', 'organization')
        # depth = 1




class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), label="User Name", required=True)
    first_name = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), label="First Name", required=True)
    last_name = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), label="Last Name", required=True)
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control'}), label="Email Address", required=True)
    password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}), label="Password", required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')



class UserRoleForm(forms.ModelForm):
    role = UserRole.objects.values_list('role', flat=True)
    class Meta:
        model = UserRole
        fields = ('role',)


