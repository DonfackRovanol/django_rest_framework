from rest_framework import serializers
from .models import entreprise

class entrepriseserializes(serializers.ModelSerializer):
    nom = serializers.CharField()
    email = serializers.EmailField()
    addresse = serializers.CharField()
    siteweb = serializers.CharField()
    image = serializers.ImageField()
    
    class Meta:
        model = entreprise
        fields = ('nom','email', 'addresse', 'siteweb', 'image')
        