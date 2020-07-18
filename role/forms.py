from django import forms
from role.models import Role


class RoleForm(forms.ModelForm):
    role_name = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), label="Role Name", required=True)
    role_description = forms.CharField(widget=forms.Textarea({'class': 'form-control'}), label="Role Description")

    class Meta:
        model = Role
        fields = ('role_name', 'role_description')




