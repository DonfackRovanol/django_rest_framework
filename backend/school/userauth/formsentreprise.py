from django import forms
from .models import entreprise

class entrpriseform (forms.ModelForm):
    class Meta:
        model = entreprise
        fields = '__all__'