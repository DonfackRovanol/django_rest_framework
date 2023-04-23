from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serialize import UserPublicSerialize
from .validators import validators_unique_product_name
from .models import product

class productserializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerialize(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validators_unique_product_name])
    class Meta:
        model = product
        fields = ('owner','email','url','pk','name', 'content', 'prix', 'my_discount')
    
    #la validation personalise des name existant dans la bd
    #def validate_name(self, value):
    #    qs = product.objects.filter(name__iexact=value)
    #    if qs.exists():
    #        raise serializers.ValidationError(f"le produit {value} existe deja en bd")
    #    return value
    
    #les 2premier methode de recuperation de l'addresse email...
    #def create(self, validated_data):
    #    print(validated_data)
    #    email = validated_data.pop('email')
    #    print(email)
    #    print(validated_data)
        #return product.objects.create(**validated_data)
    #    obj = super().create(validated_data)
    #    return obj
    
    
    #la methode de insertion un lien pour voir les details des produit...
    #def get_url(self, odj):
    #    request = self.context.get('request')
    #    if request is None:
    #        return None
    #    return reverse("product-detail", kwargs={'pk': odj.pk}, request=request)
    
    #gerer les champs SerializerMethodField pour une cle etranger user
    #def get_owner(self, obj):
    #    return {'username':obj.user.request.username, 'id':obj.user.pk}
    
    #gerer les champs SerializerMethodField
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, product):
            return None
        return obj.get_discount
    
    