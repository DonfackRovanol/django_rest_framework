from .models import product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#def validate_product_name(value):
#    qs = product.objects.filter(name__iexact=value)
#    if qs.exists():
#        raise serializers.ValidationError(f"le produit {value} existe deja en bd")
#    return value

validators_unique_product_name= UniqueValidator(queryset=product.objects.all())
