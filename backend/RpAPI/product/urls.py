from django.urls import path
from .views import *

urlpatterns = [
    #path('<int:pk>/', DetailProductView.as_view()),
    #path('create/', CreateProductView.as_view()),
    #path('update/<int:pk>/', UpdateProductView.as_view()),
    #path('delete/<int:pk>/', deleteProductView.as_view()),
    #path('list/', listProductView.as_view()),
    path('create-list/', ListCreateProductView.as_view()),
    path('<int:pk>/detail', ProductMixinsViews.as_view(), name="product-detail"),
    path('update/<int:pk>/', ProductMixinsViews.as_view(), name="product-update"),
    path('delete/<int:pk>/', ProductMixinsViews.as_view()),
    path('list/', ProductMixinsViews.as_view()),
]
