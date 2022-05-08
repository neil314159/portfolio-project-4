from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewList.as_view(), name="home"),
    path('<slug:slug>/edit/', views.ReviewUpdateView.as_view(), name="review_edit"),
    path('add/', views.ReviewCreateView.as_view(), name='publish_review'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
]
