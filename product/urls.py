from django.urls import path
from .views import (
    Home,
    ProductDetails,
    CategoryDetails
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product-details/<str:slug>/', ProductDetails.as_view(), name='product-details'),
     path('category-details/<str:slug>/', CategoryDetails.as_view(), name='category-details'),
]
