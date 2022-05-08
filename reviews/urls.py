from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewList.as_view(), name="home"),
    path('add/', views.ReviewCreateView.as_view(), name='publish_review'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
]
