from rest_framework import serializers
from product.models import product


class ProductInlineSerializer(serializers.Serializer):
    
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()
    class Meta:
        model = product
        fields = ('email', 'name')

class UserPublicSerialize(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    
    def get_user_product(self, obj):
        user = obj
        request = self.context.get('request')
        product = user.product_set.all()[:3]
        return ProductInlineSerializer(product, many=True, context={'request':request}).data