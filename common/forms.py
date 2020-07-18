from django import forms
from dynamicform.models import *

class renderForm(forms.Form):
    star = forms.ChoiceField(widget=forms.RadioSelect({'class':'kt-radio'}))

