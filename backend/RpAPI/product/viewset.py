from .models import product
from .serialize import productserializer
from rest_framework import mixins, viewsets


class ProductViewset(viewsets.ModelViewSet):
    
    """
    get -> list ->queryset
    get->retrieve
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    """
    
    queryset = product.objects.all()
    serializer_class = productserializer
    

class ProductListRestrieveViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = product.objects.all()
    serializer_class = productserializer