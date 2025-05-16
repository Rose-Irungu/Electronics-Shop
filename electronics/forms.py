from django import forms
from .models import ElectronicsData


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'price', 'image_url']


class ProductForm(forms.ModelForm):
    class Meta:
        model = ElectronicsData
        fields = ['name', 'description', 'price', 'image', 'category', ]
