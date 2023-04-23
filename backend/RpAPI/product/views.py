from django.shortcuts import render
from .models import product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from .serialize import productserializer
from rest_framework import generics, mixins
from api.mixins import *

# Create your views here.
#recherche un product
class DetailProductView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = productserializer

#inserer un product
class ListCreateProductView(StaffEditorPermissionsMixins, generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = productserializer
    
    def perform_create(self, serializer):
        email = serializer.validated_data.pop('email')
        print(email)
        name = serializer.validated_data.get('name')
        contents = serializer.validated_data.get('content') or None
        if contents is None:
            contents = name
        serializer.save(content=contents, user=self.request.user)
    

#update product
class UpdateProductView(StaffEditorPermissionsMixins, UserQuerySetMixin, generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = productserializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        contents = serializer.validated_data.get('content') or None
        if contents is None:
            contents = name
        serializer.save(content=contents)

#delete product
class deleteProductView(StaffEditorPermissionsMixins, UserQuerySetMixin, generics.DestroyAPIView):
    queryset = product.objects.all()
    serializer_class = productserializer
    lookup_field = 'pk'

#lister uniquement les product
class listProductView(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = productserializer


#les mixins: fait en une seule class tout se que les class generics font 
class ProductMixinsViews(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin):
    
    queryset = product.objects.all()
    serializer_class = productserializer
    lookup_field ='pk'
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        contents = serializer.validated_data.get('content') or None
        if contents is None:
            contents = name
        serializer.save(content=contents)
    
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        contents = serializer.validated_data.get('content') or None
        if contents is None:
            contents = name
        serializer.save(content=contents)
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

