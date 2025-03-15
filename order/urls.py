from django.urls import path
from . import views

urlpatterns = [
    path('order-list/',views.OrderListAPIView.as_view(),name='order-list'),
    path('order-create/',views.OrderCreateAPIView.as_view(),name='order-create'),
    path('order-detail/<int:order_id>/',views.OrderDetailAPIView.as_view(),name='order-detail'),
    path('order-cancel/<int:order_id>/',views.OrderCancelAPIView.as_view(),name='order-cancel')
]