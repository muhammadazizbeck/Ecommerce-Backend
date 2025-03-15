from django.urls import path
from .views import ReviewListAPIView, ReviewDeleteAPIView, ReviewCreateAPIView, ReviewUpdateAPIView

urlpatterns = [
    path("products/<int:product_id>/reviews/", ReviewListAPIView.as_view(), name="review-list"),
    path("products/<int:product_id>/reviews/create/", ReviewCreateAPIView.as_view(), name="review-create"),
    path("reviews/<int:review_id>/update/", ReviewUpdateAPIView.as_view(), name="review-update"),
    path("reviews/<int:review_id>/delete/", ReviewDeleteAPIView.as_view(), name="review-delete"),
]
