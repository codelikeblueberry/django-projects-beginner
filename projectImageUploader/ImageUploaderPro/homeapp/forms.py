from . models import ImageData
from django import forms
# create your form classes here

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageData
        fields = '__all__'
        labels = {'image_name':''}

    