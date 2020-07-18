from django import forms
from dynamicform.models import FeedbackBackgroundImage


class FeedbackBackgroundImageForm(forms.ModelForm):
    image_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Title", required=True)
    image_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Image Name",
                                 required=True)
    imageUrl = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Body Backbround Image")

    class Meta:
        model = FeedbackBackgroundImage
        fields = ('image_title', 'image_name', 'imageUrl')
