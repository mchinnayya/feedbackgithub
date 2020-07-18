from django import forms
from dynamicform.models import FeedbackLayout

class FeedbackLayoutForm(forms.ModelForm):
    description_left_1 = forms.CharField(widget=forms.Textarea({'class':'form-control'}), label="Description Left 1", required=True)
    description_left_2 = forms.CharField(widget=forms.Textarea({'class':'form-control'}), label="Description Left 2", required=True)
    description_left_3 = forms.CharField(widget=forms.Textarea({'class':'form-control'}), label="Description Left 3", required=True)
    description_right_1 = forms.CharField(widget=forms.Textarea({'class':'form-control'}), label="Description Right 1", required=True)
    description_right_2 = forms.CharField(widget=forms.Textarea({'class':'form-control'}), label="Description Right 2", required=True)
    description_right_3 = forms.CharField(widget=forms.Textarea({'class':'form-control'}), label="Description Right 3", required=True)
    class Meta:
        model = FeedbackLayout
        fields = ('__all__')