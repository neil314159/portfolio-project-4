from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewList.as_view(), name="home"),
    path('search/', views.ReviewSearchResultsListView.as_view(), name='search_results'),
    path('<slug:slug>/edit/', views.ReviewUpdateView.as_view(), name="review_edit"),
    path('<slug:slug>/delete/', views.ReviewDeleteView.as_view(), name="review_delete"),
    path('add/', views.ReviewCreateView.as_view(), name='publish_review'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    
]
