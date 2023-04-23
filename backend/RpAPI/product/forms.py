from django import forms

from backend.RpAPI.product.models import product

class productForms(forms.ModelForm):
    class Meta:
        model = product
        fields = ('name', 'content', 'prix')