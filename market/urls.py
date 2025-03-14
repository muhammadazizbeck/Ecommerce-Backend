from django.urls import path
from . import views


urlpatterns = [
    path('category-list/',views.CategoryListAPIView.as_view(),name='category-list'),
    path('product-list/',views.ProductListAPIView.as_view(),name='product-list'),
    path('product-create/',views.ProductCreateAPIView.as_view(),name='product-create'),
    path('product-detail/<int:pk>/',views.ProductDetailAPIView.as_view(),name='product-detail'),
    path('product-update/<int:pk>/',views.ProductUpdateAPIView.as_view(),name='product-update'),
    path('product-delete/<int:pk>/',views.ProductDeleteAPIView.as_view(),name='product-delete')
]