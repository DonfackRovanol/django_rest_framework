from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewset, ProductListRestrieveViewset 

router = DefaultRouter()

router.register('product-b', ProductListRestrieveViewset, basename='product-a')

print(router.urls)

urlpatterns = router.urls