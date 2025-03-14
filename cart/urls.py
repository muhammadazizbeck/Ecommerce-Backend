from django.urls import path
from . import views

urlpatterns = [
    path('cart-list/',views.CartListAPIView.as_view(),name='cart-list'),
    path('cart-add/',views.CartAddAPIView.as_view(),name='cart-add'),
    path('cart-delete/',views.CartDeleteAPIView.as_view(),name='cart-delete'),
    path('cart-item-delete/',views.CartItemDeleteAPIView.as_view(),name='cart-item-delete')
]